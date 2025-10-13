import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from src.utils.logger import get_logger
from preprocessing import *

logger = get_logger(__name__, log_file="pipeline.log")

def feature_engineering():
    #Importing the reduced dataset
    gene_pam50_redux = pd.read_csv(p("processed", "gene_pam50_redux.csv"), index_col=0)

    logger.info("Initializing train - validation - test split for the reduced dataset")

    X = gene_pam50_redux.drop('pam50 subtype', axis=1).copy()
    y = gene_pam50_redux[['pam50 subtype']].copy()
    #to ensure keeping class proportions in the split, we use stratify=y parameter
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)
    logger.info(f"X sets - Train: {X_train.shape}, Val: {X_val.shape}, Test: {X_test.shape}")
    logger.info(f"y sets - Train: {y_train.shape}, Val: {y_val.shape}, Test: {y_test.shape}")

    #Separating X_train numeric features from 'SampleID' (object) for scaling
    X_train_num = X_train.select_dtypes(include=['number'])
    X_val_num = X_val.select_dtypes(include=['number'])
    X_test_num = X_test.select_dtypes(include=['number'])

    logger.info("Scaling numerical variables")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_num)
    X_val_scaled = scaler.transform(X_val_num)
    X_test_scaled = scaler.transform(X_test_num)

    #converting again into pd.DataFrame
    X_train_scaled_df = pd.DataFrame(X_train_scaled, index=X_train.index)
    X_val_scaled_df = pd.DataFrame(X_val_scaled, index=X_val.index)
    X_test_scaled_df = pd.DataFrame(X_test_scaled, index=X_test.index)

    logger.info("Performing PCA with 50 components for around 60 percent of variance explained")
    pca_2 = PCA(n_components=50)
    X_train_pca = pca_2.fit_transform(X_train_scaled_df)

    X_train_pca_df = pd.DataFrame(X_train_pca, columns=[f"PC{i+1}" for i in range(50)], index=X_train.index)

    #getting x_val and x_test scaled
    X_val_pca = pca_2.transform(X_val_scaled)
    X_test_pca = pca_2.transform(X_test_scaled)

    #Also naming columns with Principal Components
    X_val_pca_df = pd.DataFrame(X_val_pca, columns=[f"PC{i+1}" for i in range(50)], index=X_val.index)
    X_test_pca_df = pd.DataFrame(X_test_pca, columns=[f"PC{i+1}" for i in range(50)], index=X_test.index)

    logger.info("Exporting X_train_pca, X_val_pca, X_test_pca, y_train, y_val, y_test")

    X_train_pca_df.to_csv(p("processed", "X_train_pc.csv"))
    X_val_pca_df.to_csv(p("processed", "X_val_pc.csv"))
    X_test_pca_df.to_csv(p("processed", "X_test_pc.csv"))

    y_train.to_csv(p("processed", "y_train.csv"))
    y_val.to_csv(p("processed", "y_val.csv"))
    y_test.to_csv(p("processed","y_test.csv"))
    


