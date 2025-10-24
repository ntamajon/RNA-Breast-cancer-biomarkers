from zenml import step
from pipelines.etl.main_etl import main_etl

@step
def load_data():
    gene_df = main_etl()
    return gene_df