from typing import Callable
import datetime as dt
import pandas as pd
from functools import reduce, partial
import babel.dates
import i18n


class DataSchema:
    AMOUNT = "amount"
    CATEGORY = "category"
    DATE = "date"
    MONTH = "month"
    YEAR = "year"


Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]


def create_year_column(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.YEAR] = df[DataSchema.DATE].dt.year.astype(str)
    return df


def create_month_column(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.MONTH] = df[DataSchema.DATE].dt.month.astype(str)
    return df


def translate_date(df: pd.DataFrame, locale: str) -> pd.DataFrame:
    def date_repr(date: dt.date) -> str:
        return babel.dates.format_date(date, format="MMMM", locale=locale)

    df[DataSchema.MONTH] = df[DataSchema.DATE].apply(date_repr)
    return df


def translate_category(df: pd.DataFrame) -> pd.DataFrame:
    def translate(category: str) -> str:
        return i18n.t(f"category.{category}")

    df[DataSchema.CATEGORY] = df[DataSchema.CATEGORY].apply(translate)
    return df


def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def load_transaction_data(path: str, locale: str) -> pd.DataFrame:
    # load the data from a CSV file
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.AMOUNT: float,
            DataSchema.CATEGORY: str,
            DataSchema.DATE: str,
        },
        parse_dates=[DataSchema.DATE],
    )
    # NOTE: using a compose
    preprocessor = compose(
        # NOTE: using partial to normalize function
        create_year_column,
        create_month_column,
        partial(translate_date, locale=locale),
        translate_category,
    )
    return preprocessor(data)
