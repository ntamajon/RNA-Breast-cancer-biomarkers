import pandas as pd
import numpy as np
import os
from src.utils.logger import get_logger
from src.utils.path_utils import p
from etl.export import *

logger = get_logger(__name__, log_file="pipeline.log")

logger.info("Initializing data preprocessing for training...")

def data_preprocessing() -> pd.DataFrame:
    gene_pam50 = pd.read_csv(p("processed", "gene_pam50.csv"))

    #numeric columns
    num_cols = list(gene_pam50.columns[1: (len(gene_pam50.columns)-1)])

    #getting expressed genes
    logger.info("Getting number of expressed genes for criterion 1 - log2(TPM + 1) > 1")
    gene_pam50['expressed_genes_h1'] = gene_pam50.apply(lambda row: np.sum(row[col] > 1 for col in num_cols), axis=1)
    
    logger.info("Finding the percentage of samples where each gene is higher than 1")
    gene_expressed_props = ((gene_pam50[num_cols] > 1).sum(axis=0) / len(gene_pam50) * 100).round(2)

    logger.info("Reducing the dataset by removing genes with less than 20 percent expression among samples")

    cols_to_keep = gene_expressed_props[gene_expressed_props >= 20].index
    gene_pam50_redux = gene_pam50[cols_to_keep]

    logger.info(f"New reduced dataset has {gene_pam50_redux.shape[1]} columns")

    #adding 'SampleID' and 'pam50 subtype'
    gene_pam50_redux.insert(0, 'SampleID', gene_pam50['SampleID'])
    gene_pam50_redux.insert(13622, 'pam50 subtype', gene_pam50['pam50 subtype'])

    logger.info("Exporting reduced dataset")
    #exporting reduced dataset
    gene_pam50_redux.to_csv(p("processed","gene_pam50_redux.csv"))

