import pandas as pd
import numpy as np
from src.utils.logger import get_logger
from src.utils.path_utils import p

logger = get_logger(__name__, log_file="pipeline.log")

def sample_cleaner(gene_df) -> pd.DataFrame:
    """
    Cleans gene data file
    """
    logger.info("Checking missing gene data for gene expression file...")
    gexp_columns = gene_df.columns

    missing_samples = []
    for col in gexp_columns:
        if np.sum(gene_df[col].isnull()) > 0:
            missing_samples.append(col)

    if len(missing_samples) > 0:
        raise ValueError(f"{missing_samples} has missing gene data")
    else:
        logger.info("No missing gene data")

    return gene_df

def metadata_cleaner(metadata) -> pd.DataFrame:
    """
    Cleans metadata files
    """
    
    logger.info("Cleaning column names on metadata files...")
    metadata.rename(columns=lambda x: x.replace('"', ''), inplace=True)

    logger.info("Cleaning column values")
    for col in metadata.select_dtypes(include=['object']):
        metadata[col] = metadata[col].str.replace('"', '', regex=False)

    print(f"{metadata} has {metadata.shape} samples")

    return metadata





