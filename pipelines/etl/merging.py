import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__, log_file="pipeline.log")

def merging(metadata_1, metadata_2, gene_df):

    logger.info("Concatenating metadata...")
    clinic_data = pd.concat([metadata_1, metadata_2], axis=0, ignore_index=True)
    logger.info("Filtering SampleID and nhg prediction mgc")
    clinic_data_nhg = clinic_data[['SampleID', 'nhg prediction mgc']]
    logger.info("Merging with gene data by Sample ID")
    gene_pam50 = pd.merge(gene_df, clinic_data_nhg, on='SampleID', how='inner')

    return pd.DataFrame(gene_pam50)