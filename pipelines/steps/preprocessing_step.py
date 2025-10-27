from zenml import step
from pipelines.preprocessing import data_preprocessing
from pipelines.steps.load_data_steps import load_data
import pandas as pd


@step
def preprocessing(gene_df: pd.DataFrame) -> pd.DataFrame:
    gene_df_processed = data_preprocessing(gene_df)
    return gene_df_processed