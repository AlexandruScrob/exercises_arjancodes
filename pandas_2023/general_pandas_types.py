from pathlib import Path

import pandas as pd


def read_airports_dataset(path: Path, filename: str) -> pd.DataFrame:
    """Read the Netherlands airport dataset csv file as a pandas dataframe."""

    return pd.read_csv(path / filename)


def remove_metadata_information(path: Path, filename: str) -> pd.DataFrame:
    """
    Skips the metadata information in Netherlands airport csv file while reading it.
    """

    return pd.read_csv(path / filename, skiprows=2)


def main() -> None:
    dataset_path = Path(__file__).resolve().parent / "datasets"
    filename = "netherlands_airports.csv"

    aiports_wrong_type_infer = read_airports_dataset(dataset_path, filename)

    print("---Wrong types infered by pandas---")
    print(aiports_wrong_type_infer.info(), end="\n\n")

    airports_raw = remove_metadata_information(dataset_path, filename)
    airports_raw.columns = aiports_wrong_type_infer.columns
    print("---Types after removing the metadata row---")
    print(airports_raw.info(), end="\n\n")

    mapping_types_conversion = {
        "ident": "string",
        "type": "string",
        "name": "string",
        "continent": "string",
        "iso_country": "string",
        "iso_region": "string",
        "municipality": "string",
        "gps_code": "string",
        "iata_code": "string",
        "local_code": "string",
        "home_link": "string",
        "wikipedia_link": "string",
        "keywords": "string",
        "scheduled_service": "boolean",
        # "last_updated": "datetime",
    }

    airports_types_converted = airports_raw.astype(mapping_types_conversion)

    airports_types_converted["last_updated"] = pd.to_datetime(
        airports_types_converted["last_updated"]
    )

    print("---Types after conversion---")
    print(airports_types_converted.info(), end="\n\n")


if __name__ == "__main__":
    main()
