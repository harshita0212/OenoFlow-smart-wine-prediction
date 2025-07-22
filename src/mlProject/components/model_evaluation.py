import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

# import mlflow
# import mlflow.sklearn
# import pandas as pd
# import numpy as np
# import joblib
import json

from pathlib import Path
# from urllib.parse import urlparse
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Helper to save scores locally
def save_json(path: Path, data: dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted = model.predict(test_x)
            rmse, mae, r2 = self.eval_metrics(test_y, predicted)
            #RMSE: How far predictions are from actual values (in same unit as target).
            #MAE: Average absolute error.
            #R² Score: How well your model explains the variance in the data (closer to 1 = better).

            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            self.config.metric_file_name.parent.mkdir(parents=True, exist_ok=True)
            save_json(self.config.metric_file_name, scores)


            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # 💡 Save model manually & log as artifact
            model_path = Path("models/sk_model.pkl")
            model_path.parent.mkdir(parents=True, exist_ok=True)
            joblib.dump(model, model_path)
            mlflow.log_artifact(str(model_path))
