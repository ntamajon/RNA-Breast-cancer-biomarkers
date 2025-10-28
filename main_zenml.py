from pipelines.zenml_pipelines.training_pipeline import training_pipeline
from pipelines.steps.load_data_steps import load_data
from pipelines.steps.preprocessing_step import preprocessing
from pipelines.zenml_pipelines.training_pipeline import training_pipeline

if __name__ == "__main__":
    training_pipeline()
