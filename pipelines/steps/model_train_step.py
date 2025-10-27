from zenml import step
import pandas as pd
from pipelines.model_train import model_train
from typing import Any

@step
def model_train_step(
    X_train: pd.DataFrame,
    X_val: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_val: pd.Series,
    y_test: pd.Series
) -> Any:
    f1, report, matrix = model_train(X_train, X_val, X_test, y_train, y_val, y_test)
    return f1, report, matrix


    