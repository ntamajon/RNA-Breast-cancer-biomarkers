from zenml import step
import pandas as pd
from pipelines.feature_engineering import feature_engineering
from pipelines.steps.preprocessing_step import preprocessing

@step
def feature_engineering_step() -> pd.DataFrame:
    gene_df_processed = preprocessing()
    X_train, X_val, X_test, y_train, y_val, y_test = feature_engineering(gene_df_processed)
    return X_train, X_val, X_test, y_train, y_val, y_test