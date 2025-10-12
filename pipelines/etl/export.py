import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__, log_file="pipeline.log")

def exporter(gene_df, file_path):
    gene_df.to_csv("gene_df.csv", index=False)


    
