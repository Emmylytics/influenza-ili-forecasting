# Import libraries
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent


RAW_DATA = PROJECT_ROOT / "data" / "raw"
CLEANED_DATA = PROJECT_ROOT / "data" / "cleaned"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"


def load_ilinet(filename: str = "ILINet.csv") -> pd.DataFrame:
    """
    Load the ILINet dataset from the raw data directory.
    """
    return pd.read_csv(RAW_DATA / filename, skiprows=1)



def load_cleaned_ilinet(filename: str = "ILINet_cleaned.csv") -> pd.DataFrame:
    """
    Load the cleaned ILINet dataset.
    """
    return pd.read_csv(CLEANED_DATA / filename)



def load_processed_ilinet(filename: str = "ILINet_processed.csv") -> pd.DataFrame:
    """
    Load the preprocessed ILINet dataset.
    """
    return pd.read_csv(PROCESSED_DATA / filename, parse_dates=["DATE"])