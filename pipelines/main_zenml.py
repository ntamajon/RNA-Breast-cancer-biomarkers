from pipelines.zenml_pipelines.training_pipeline import training_pipeline
from pipelines.steps.load_data_steps import load_data
from pipelines.steps.preprocessing_step import preprocessing
from pipelines.steps.feature_eng_step import feature_engineering_step
from pipelines.steps.model_train_step import model_train_step

if __name__ == "__main__":
    run = training_pipeline(
        load_data=load_data(),
        preprocessing=preprocessing(),
        feature_engineering_step=feature_engineering_step(),
        model_train_step=model_train_step()
    )
    run.run()