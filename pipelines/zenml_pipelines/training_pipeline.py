from zenml import pipeline
from pipelines.steps.load_data_steps import load_data
from pipelines.steps.preprocessing_step import preprocessing
from pipelines.steps.feature_eng_step import feature_engineering_step
from pipelines.steps.model_train_step import model_train_step

@pipeline
def training_pipeline():
    gene_df = load_data()
    gene_df_processed = preprocessing(gene_df)

    #returning split and reduced dataset with pca
    X_train, X_val, X_test, y_train, y_val, y_test = feature_engineering_step(gene_df_processed)

    model_train_step(X_train, X_val, X_test, y_train, y_val, y_test) 