from zenml import step
import pandas as pd
from typing import Tuple
from pipelines.feature_engineering import feature_engineering

@step
def feature_engineering_step(
    gene_df: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    try:
        print("Starting feature engineering...")

        X_train, X_val, X_test, y_train, y_val, y_test = feature_engineering(gene_df)

        #Ensure correct types for y
        if isinstance(y_train, pd.DataFrame):
            y_train = y_train.squeeze()
        if isinstance(y_val, pd.DataFrame):
            y_val = y_val.squeeze()
        if isinstance(y_test, pd.DataFrame):
            y_test = y_test.squeeze()

        print("✅ Finished feature engineering.")
        return (X_train, X_val, X_test, y_train, y_val, y_test)

    except Exception as e:
        print("Error in feature_engineering_step:", e)
        raise e