from pathlib import Path

import pandas as pd
import pandera as pa

from altered_schema import schema


@pa.check_output(schema, lazy=True)
def retrieve_retail_products(path: Path | str) -> pd.DataFrame:
    return pd.read_csv(path)


def main() -> None:
    dataset_path = Path(__file__).resolve().parent / "datasets"

    products = retrieve_retail_products(dataset_path / "online_retail.csv")

    print(products.head())


if __name__ == "__main__":
    main()
