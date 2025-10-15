from pipelines.etl.main_etl import main_etl
from src.utils.logger import get_logger
from pipelines import preprocessing, feature_engineering, model_train
import pandas as pd
import numpy as np
from src.utils.path_utils import p

logger = get_logger("pipeline", log_file="pipeline.log")

def main():
    logger.info("Starting full pipeline (ETL -> Preprocessing -> FE -> Training)...")
    gene_path = input("Insert name of gene file with extension:")
    gene_path = str(gene_path)
    meta_path_1 = input("Insert name of metadata1 file with extension:")
    meta_path_1 = str(meta_path_1)
    meta_path_2 = input("Insert name of metadata2 file with extension:")
    meta_path_2 = str(meta_path_2)

    #from etl/main.py
    gene_pam50 = main_etl(gene_path, meta_path_1, meta_path_2)

    #from preprocessing.py
    gene_pam50_redux = preprocessing.data_preprocessing(gene_pam50=gene_pam50)

    #from feature_engineering.py
    X_train, X_val, X_test, y_train, y_val, y_test = (
        feature_engineering.feature_engineering(gene_pam50_redux)
    )

    #from model_train.py
    model_train.model_train(X_train, X_val, X_test, y_train, y_val, y_test)
    logger.info("Pipeline completed.")




if __name__ == "__main__":
    main()
