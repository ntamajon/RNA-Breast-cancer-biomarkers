import pandas as pd
import numpy as np
import os
from src.utils.logger import get_logger
from src.utils.path_utils import p

logger = get_logger("pipeline", log_file="pipeline.log")

def data_export(merged_file):
    """
    Exports data to ETL folder
    """
    logger.info("Exporting dataset ready for analysis...")

    output_path = p("processed", "gene_pam50.csv")
    merged_file.to_csv(output_path, index=False)

    return logger.info(f"Exported file in: {output_path}")


    
