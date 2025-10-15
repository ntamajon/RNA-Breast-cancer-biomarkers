import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from sklearn.pipeline import Pipeline
from src.utils.logger import get_logger
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.metrics import classification_report, confusion_matrix, f1_score

logger = get_logger(__name__, log_file="pipeline.log")

def model_train(X_train_pc, X_val_pc, X_test_pc, y_train, y_val, y_test):
    
    logger.info("Encoding labels...")
    le = LabelEncoder()
    y_train_enc = le.fit_transform(y_train)
    y_val_enc = le.transform(y_val)

    logger.info(le.classes_)

    logger.info("Balancing classes for better performance...")
    smote = SMOTE(random_state=42, sampling_strategy={0: 600, 1: 600, 2: 1196, 3: 600, 4: 500})
    X_train_res, y_train_res = smote.fit_resample(X_train_pc, y_train_enc)

    xgb_smoted = XGBClassifier(
    objective="multi:softmax",  # for multiclass
    num_class=5, 
    n_estimators=500,
    learning_rate=0.01,
    max_depth=3,
    subsample=0.6,
    colsample_bytree=0.7,
    random_state=42,
    use_label_encoder=False,
    eval_metric="mlogloss",
    #early_stopping_rounds=20,
    min_child_weight=5,
    min_split_loss=1,
    reg_alpha=4,
    reg_lambda=20)

    #Training the model
    logger.info("Training the model...")
    xgb_smoted.fit(X_train_res, y_train_res)

    # Predictions
    logger.info("Getting predictions...")
    y_val_pred_xgb_smoted = xgb_smoted.predict(X_val_pc)

    #Metrics
    logger.info("Getting metrics on validation set...")
    f1_smoted = f1_score(y_val_enc, y_val_pred_xgb_smoted, average="macro")

    logger.info(f"Validation Macro F1: {round(f1_smoted, 4)}")
    logger.info(classification_report(y_val_enc, y_val_pred_xgb_smoted))
    logger.info(confusion_matrix(y_val_enc, y_val_pred_xgb_smoted))


    