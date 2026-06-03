import json
from pathlib import Path

from dataclasses import dataclass

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


@dataclass(frozen=True)
class TrainingConfig:
    data_path: Path
    output_dir: Path
    test_size: float = 0.2
    random_state: int = 42

    def __post_init__(self) -> None:
        if not self.data_path.exists():
            raise FileNotFoundError(f"Dataset not found: {self.data_path}")
        if self.data_path.suffix != ".csv":
            raise ValueError("data_path must point to a CSV file")
        if not self.output_dir.parent.exists():
            raise FileNotFoundError(
                f"Parent directory for output_dir does not exist: {self.output_dir.parent}"
            )
        if not 0 < self.test_size < 1:
            raise ValueError("test_size must be between 0 and 1")
        if self.random_state < 0:
            raise ValueError("random_state must be >= 0")

    @property
    def model_path(self) -> Path:
        return self.output_dir / "churn_model.joblib"

    @property
    def metrics_path(self) -> Path:
        return self.output_dir / "metrics.json"

    @property
    def importances_path(self) -> Path:
        return self.output_dir / "feature_importances.csv"

    def make_output_dir(self) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)


# Data loading
def load_data(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)


# Preprocessing
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned = cleaned.drop_duplicates(subset=["customer_id"])
    cleaned = cleaned.dropna(subset=["churn"])

    cleaned["tenure"] = cleaned["tenure"].fillna(cleaned["tenure"].median())
    cleaned["monthly_charges"] = cleaned["monthly_charges"].fillna(
        cleaned["monthly_charges"].median()
    )
    cleaned["support_tickets"] = cleaned["support_tickets"].clip(lower=0, upper=15)

    return cleaned


def run(config: TrainingConfig) -> None:
    print("Running churn experiment...\n")

    config.make_output_dir()

    df = load_data(config.data_path)
    df_clean = clean_data(df)
    df_features = engineer_features(df_clean)
    df_encoded = encode_categorical_features(df_features)
    X, y = split_features_and_target(df_encoded)
    X_train, X_test, y_train, y_test = split_data(
        X,
        y,
        test_size=config.test_size,
        random_state=config.random_state,
    )

    model = build_model(random_state=42)
    trained_model = train_model(model, X_train, y_train)
    metrics = evaluate_model(trained_model, X_test, y_test)
    save_artifacts(trained_model, config, metrics, X.columns.tolist())
    print_summary(trained_model, config.output_dir, metrics, X.columns.tolist())


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    prepared = df.copy()

    prepared["charges_per_ticket"] = prepared["monthly_charges"] / (
        prepared["support_tickets"] + 1
    )
    prepared["is_senior"] = (prepared["age"] >= 65).astype(int)
    prepared["is_new_customer"] = (prepared["tenure"] < 6).astype(int)

    return prepared


def encode_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    df = pd.get_dummies(
        df,
        columns=["contract_type", "internet_service", "payment_method"],
        drop_first=True,
    )

    return df


def split_features_and_target(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series]:
    X = df.drop(columns=["customer_id", "churn"])
    y = df["churn"]

    return X, y


# Training
def split_data(
    X: pd.DataFrame, y: pd.Series, test_size: float, random_state: int
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )


def build_model(random_state: int) -> RandomForestClassifier:
    return RandomForestClassifier(
        n_estimators=100,
        max_depth=7,
        min_samples_split=10,
        random_state=random_state,
    )


def train_model(
    model: RandomForestClassifier, X_train: pd.DataFrame, y_train: pd.Series
) -> RandomForestClassifier:
    model.fit(X_train, y_train)
    return model


# Evaluation
def evaluate_model(
    model: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series
) -> dict[str, object]:
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True)

    return {
        "accuracy": accuracy,
        "classification_report": report,
    }


def compute_feature_importances(
    model: RandomForestClassifier,
    feature_names: list[str],
) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "feature": feature_names,
            "importance": model.feature_importances_,
        }
    ).sort_values("importance", ascending=False)


# Persistence
def save_artifacts(
    model: RandomForestClassifier,
    config: TrainingConfig,
    metrics: dict[str, object],
    feature_names: list[str],
) -> None:

    joblib.dump(model, config.model_path)

    with config.metrics_path.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    importances = pd.DataFrame(
        {
            "feature": feature_names,
            "importance": model.feature_importances_,
        }
    ).sort_values("importance", ascending=False)

    importances.to_csv(config.importances_path, index=False)


def print_summary(
    model: RandomForestClassifier,
    output_dir: Path,
    metrics: dict[str, object],
    feature_names: list[str],
) -> None:
    print("Evaluation results:")
    print(f"Accuracy: {metrics['accuracy']:.3f}\n")

    report = metrics["classification_report"]
    print("Precision / Recall / F1:")
    print(
        f"Class 0 -> precision={report['0']['precision']:.3f}, "
        f"recall={report['0']['recall']:.3f}, "
        f"f1={report['0']['f1-score']:.3f}"
    )
    print(
        f"Class 1 -> precision={report['1']['precision']:.3f}, "
        f"recall={report['1']['recall']:.3f}, "
        f"f1={report['1']['f1-score']:.3f}\n"
    )

    importances = compute_feature_importances(model, feature_names)

    print("Top 10 feature importances:")
    print(importances.head(10).to_string(index=False), "\n")

    print(f"Artifacts saved in: {output_dir.resolve()}")


def main() -> None:
    config = TrainingConfig(
        data_path=Path("data/churn.csv"),
        output_dir=Path("artifacts"),
        test_size=0.25,
        random_state=42,
    )

    run(config)


if __name__ == "__main__":
    main()
