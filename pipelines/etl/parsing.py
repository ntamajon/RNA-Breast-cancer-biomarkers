import gzip
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__, log_file="pipeline.log")

def parse_series_matrix(file_path_txt_gz, file_path_csv):
    logger.info("Initializing decompression for txt.gz files...")
    with gzip.open(file_path_txt_gz, "rt") as f: 
        for line in f:
            if line.startswith("!"):
                print(line.strip())

    logger.info("Loading .csv files...")
    gene_df = pd.read_csv(file_path_csv)
    
    logger.info("Reading the file per line")
    with gzip.open(file_path_txt_gz, "rt") as f:
        lines = [l.strip() for l in f if l.startswith("!Sample_")]

    # títulos de muestras
    sample_titles = [l.split("\t")[1:] for l in lines if l.startswith("!Sample_title")][0]

    metadata = {"SampleID": sample_titles}

    for line in lines:
        if line.startswith("!Sample_characteristics_ch1"):
            parts = line.split("\t")[1:]  # ignorar "!Sample_characteristics_ch1"
            # el nombre de la característica está antes de los ":"
            first_val = parts[0]
            if ":" in first_val:
                key = first_val.split(":")[0].strip()
                values = [p.split(":",1)[1].strip() if ":" in p else p for p in parts]
                metadata[key] = values

    return pd.DataFrame(metadata, gene_df)