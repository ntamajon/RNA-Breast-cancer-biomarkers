from zenml import step
from pipelines.etl.main_etl import main_etl
import pandas as pd

@step
def load_data(gene_path: str, meta_path_1: str, meta_path_2: str):
    gene_df = main_etl(gene_path, meta_path_1, meta_path_2)

    return gene_df