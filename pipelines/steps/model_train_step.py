from zenml import step
import pandas as pd
from pipelines.model_train import model_train
from pipelines.steps.feature_eng_step import feature_engineering_step

@step
def model_train_step():
    X_train, X_val, X_test, y_train, y_val, y_test = feature_engineering_step()
    f1, report, matrix = model_train(X_train, X_val, X_test, y_train, y_val, y_test)
    return f1, report, matrix


    