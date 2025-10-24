from zenml import step
from pipelines.preprocessing import data_preprocessing
from pipelines.steps.load_data_steps import load_data


@step
def preprocessing():
    gene_df = load_data()
    gene_df_processed = data_preprocessing(gene_df)
    return gene_df_processed