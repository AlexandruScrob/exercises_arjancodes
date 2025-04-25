from datetime import datetime
from pathlib import Path

import pandas as pd
import pandera as pa

from pandera.typing import DataFrame, Series


class OutputSchema(pa.SchemaModel):
    """Schema for retail products dataset."""

    InvoiceNo: Series[str]
    StockCode: Series[str] = pa.Field(nullable=True)
    Description: Series[str] = pa.Field(nullable=True)
    Quantity: Series[int] = pa.Field(ge=1)
    InvoiceDate: Series[datetime]
    UnitPrice: Series[float]
    CustomerID: Series[float] = pa.Field(nullable=True)
    Country: Series[pd.StringDtype]


@pa.check_types(lazy=True)  # uses the type annotation for which type to use
def retrieve_retail_products(path: Path | str) -> DataFrame[OutputSchema]:
    return pd.read_csv(path)


def main() -> None:
    try:
        dataset_path = Path(__file__).resolve().parent / "datasets"

        products = retrieve_retail_products(dataset_path / "online_retail.csv")

        print(products.head())
    except pa.errors.SchemaErrors as err:
        print(err)


if __name__ == "__main__":
    main()
