import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__, log_file="pipeline.log")

def data_cleaner(metadata):
        logger.info("Cleaning column names")
        metadata.rename(columns=lambda x: x.replace('"', ''), inplace=True)

        logger.info("Cleaning column values")
        for col in metadata.select_dtypes(include=['object']):
            metadata[col] = metadata[col].str.replace('"', '', regex=False)

        return pd.DataFrame(metadata)