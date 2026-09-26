import pandas as pd
import numpy as np
import os


RAW_PATH = "../data/raw/tomato_prices.csv"
PROCESSED_PATH = "../data/processed/tomato_clean.csv"


def load_data():
    """Load the raw agricultural dataset."""
    df = pd.read_csv(RAW_PATH)
    return df


def clean_column_names(df):
    """Standardize column names."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("/", "_", regex=False)
    )

    return df


def remove_duplicates(df):
    """Remove duplicate records."""
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"Removed duplicates: {before - after}")

    return df


def handle_dates(df):
    """Convert date column into datetime format."""
    if "date" in df.columns:
        df["date"] = pd.to_datetime(
            df["date"],
            errors="coerce"
        )

        df = df.dropna(subset=["date"])

    return df


def handle_numeric_columns(df):
    """Convert price-related columns to numeric values."""

    numeric_columns = [
        "min_price",
        "max_price",
        "modal_price",
        "arrival_quantity"
    ]

    for column in numeric_columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    return df


def remove_invalid_prices(df):
    """Remove records containing invalid prices."""

    if "modal_price" in df.columns:

        df = df[df["modal_price"] > 0]

    return df


def create_time_features(df):
    """Create useful time-based ML features."""

    if "date" in df.columns:

        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["day"] = df["date"].dt.day
        df["day_of_week"] = df["date"].dt.dayofweek

    return df


def create_price_features(df):
    """Create additional price-related features."""

    if "min_price" in df.columns and "max_price" in df.columns:

        df["price_range"] = (
            df["max_price"] - df["min_price"]
        )

        df["average_price"] = (
            df["min_price"] + df["max_price"]
        ) / 2

    return df


def save_data(df):

    os.makedirs(
        os.path.dirname(PROCESSED_PATH),
        exist_ok=True
    )

    df.to_csv(
        PROCESSED_PATH,
        index=False
    )

    print(
        f"Processed dataset saved to: {PROCESSED_PATH}"
    )


def main():

    print("Loading dataset...")

    df = load_data()

    print("Original shape:", df.shape)

    df = clean_column_names(df)

    df = remove_duplicates(df)

    df = handle_dates(df)

    df = handle_numeric_columns(df)

    df = remove_invalid_prices(df)

    df = create_time_features(df)

    df = create_price_features(df)

    print("Final shape:", df.shape)

    print("\nFinal columns:")
    print(df.columns.tolist())

    save_data(df)


if __name__ == "__main__":
    main()
