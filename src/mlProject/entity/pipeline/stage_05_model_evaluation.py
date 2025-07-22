from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

from mlProject.config.configuration import ConfigurationManager

config = ConfigurationManager()
model_eval_config = config.get_model_evaluation_config()

import mlflow
import os

os.environ["MLFLOW_TRACKING_USERNAME"] = "harshita0212"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "a96f4207556acabc9f145184bde3390ce52c2f88"  # Keep it safe

mlflow.set_tracking_uri("https://dagshub.com/harshita0212/OenoFlow-smart-wine-prediction.mlflow")

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
       config = ConfigurationManager()
       model_eval_config = config.get_model_evaluation_config()
       evaluator = ModelEvaluation(config=model_eval_config)
       evaluator.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

