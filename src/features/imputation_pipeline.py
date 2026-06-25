import pandas as pd
from sklearn.impute import SimpleImputer

def impute_missing(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["is_imputed"] = df.isna().any(axis=1).astype(int)

    num_cols = df.select_dtypes(include=["float", "int"]).columns
    cat_cols = df.select_dtypes(include=["object"]).columns

    num_imputer = SimpleImputer(strategy="median")
    cat_imputer = SimpleImputer(strategy="most_frequent")

    df[num_cols] = num_imputer.fit_transform(df[num_cols])
    df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

    return df
