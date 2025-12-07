import json
from datetime import datetime
from typing import Any, Protocol
import pandas as pd


class SalesReader(Protocol):
    def read(self, input_file: str) -> pd.DataFrame: ...


class CsvSalesReader:
    def read(self, input_file: str) -> pd.DataFrame:
        return pd.read_csv(input_file, parse_dates=["date"])


class ReportWriter(Protocol):
    def write(self, output_file, data: dict[str, Any]) -> None: ...


class JsonReportWriter:
    def write(self, output_file, data: dict[str, Any]) -> None:
        with open(output_file, "w") as f:
            json.dump(data, f, indent=2)


class DateRangeFilter:
    def __init__(
        self,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
    ) -> None:
        self.start_date = start_date
        self.end_date = end_date

    def compute(self, df: pd.DataFrame) -> dict[str, Any]:
        if self.start_date:
            df = df[df["date"] >= pd.Timestamp(self.start_date)]
        if self.end_date:
            df = df[df["date"] <= pd.Timestamp(self.end_date)]

        return {
            "report_start": (
                self.start_date.strftime("%Y-%m-%d") if self.start_date else "N/A"
            ),
            "report_end": (
                self.end_date.strftime("%Y-%m-%d") if self.end_date else "N/A"
            ),
        }


class Metric(Protocol):
    def compute(self, df: pd.DataFrame) -> dict[str, Any]: ...


class CustomerCountMetric:
    def compute(self, df: pd.DataFrame) -> dict[str, Any]:
        return {"number_of_customers": df["name"].nunique()}


class AverageOrderValueMetric:
    def compute(self, df: pd.DataFrame) -> dict[str, Any]:
        avg_order = (
            0 if df[df["price"] > 0].empty else df[df["price"] > 0]["price"].mean()
        )

        return {"average_order_value (pre-tax)": round(avg_order, 2)}


class ReturnPercentageMetric:
    def compute(self, df: pd.DataFrame) -> dict[str, Any]:
        returns = df[df["price"] < 0]
        return_pct = (len(returns) / len(df)) * 100 if len(df) > 0 else 0

        return {"percentage_of_returns": round(return_pct, 2)}


class TotalSalesMetric:
    def compute(self, df: pd.DataFrame) -> dict[str, Any]:
        total_sales = df["price"].sum()

        return {"total_sales_in_period (pre-tax)": round(total_sales, 2)}


class SalesReport:
    def __init__(
        self,
        reader: SalesReader,
        writer: ReportWriter,
        metrics: list[Metric],
    ) -> None:
        self.metrics = metrics
        self.reader = reader
        self.writer = writer

    def generate(
        self,
        input_file: str,
        output_file: str,
        filter_obj: DateRangeFilter | None = None,
    ) -> None:
        df = self.reader.read(input_file)

        metrics = (*self.metrics, filter_obj) if filter_obj else self.metrics
        report_data = {}
        for metric in metrics:
            report_data |= metric.compute(df)

        self.writer.write(output_file, data=report_data)


def main() -> None:
    report = SalesReport(
        metrics=[
            CustomerCountMetric(),
            AverageOrderValueMetric(),
            ReturnPercentageMetric(),
            TotalSalesMetric(),
        ],
        reader=CsvSalesReader(),
        writer=JsonReportWriter(),
    )
    report.generate(
        input_file="sales_data.csv",
        output_file="sales_report.json",
        filter_obj=DateRangeFilter(
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 12, 31),
        ),
    )


if __name__ == "__main__":
    main()
