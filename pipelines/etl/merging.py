import pandas as pd
import numpy as np
from src.utils.logger import get_logger

logger = get_logger(__name__, log_file="pipeline.log")

def data_merge(metadata_1, metadata_2, gene_df) -> pd.DataFrame:
    """
    Merges metadata_1 with metadata_2, selects the columns
    'SampleID' and 'nhg prediction mgc'(tumor target) 
    then merges with gene expression dataset.
    """

    logger.info("Concatenating metadata...")
    clinic_data = pd.concat([metadata_1, metadata_2], axis=0, ignore_index=True)

    logger.info("Filtering SampleID and pam50 subtype...")
    clinic_data_pam50 = clinic_data[['SampleID', 'pam50 subtype']]


    logger.info("Merging with gene data by Sample ID")
    gene_merged = pd.merge(gene_df, clinic_data_pam50, on='SampleID', how='inner')

    return gene_merged
