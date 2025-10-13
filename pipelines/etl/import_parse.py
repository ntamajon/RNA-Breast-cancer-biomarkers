import gzip
import pandas as pd
from src.utils.path_utils import p
from src.utils.logger import get_logger

logger = get_logger(__name__, log_file="pipeline.log")

logger.info("Loading and decompressing files...")
def read_gene(path) -> pd.DataFrame:
    try:
        gene_df = pd.read_csv(path)
    except FileNotFoundError:
        logger.error("File doesn't exist")
    return gene_df

def parse_series_matrix(file_path) -> pd.DataFrame:
    """
    imports metadata with labels and gene expression
    """
    
    logger.info("Reading the file per line")
    with gzip.open(file_path, "rt") as f:
        lines = [l.strip() for l in f if l.startswith("!Sample_")]

    # tsample titles
    sample_titles = [l.split("\t")[1:] for l in lines if l.startswith("!Sample_title")][0]

    metadata = {"SampleID": sample_titles}

    logger.info("Reading through the file looking for the labels...")
    for line in lines:
        if line.startswith("!Sample_characteristics_ch1"):
            parts = line.split("\t")[1:]  # ignoring "!Sample_characteristics_ch1"
            # getting name of characteristic before the ":"
            first_val = parts[0]
            if ":" in first_val:
                key = first_val.split(":")[0].strip()
                values = [p.split(":",1)[1].strip() if ":" in p else p for p in parts]
                metadata[key] = values
    logger.info("Succesfully imported!")
    return pd.DataFrame(metadata)