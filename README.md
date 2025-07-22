
```markdown
```
# 🍷 OenoFlow – Smart Wine Quality Prediction

OenoFlow is a complete end-to-end Machine Learning pipeline for predicting wine quality using ML models. It is built using Python, MLflow, DVC for versioning, and deployed with Flask on an AWS EC2 instance.

---

## 🚀 Project Features

- Predicts wine quality from chemical features
- Uses ElasticNet Regression
- Experiment tracking with MLflow (hosted on DagsHub)
- Data versioning with DVC
- Modular & scalable code structure
- Packaged as a Flask web app
- Deployed on AWS EC2

---
```
## 📁 Project Structure

```

OenoFlow-smart-wine-prediction/
│
├── artifacts/                  # All pipeline outputs
├── config/                    # YAML configuration files
├── data/                      # Raw datasets (not tracked by git)
├── mlruns/                    # MLflow tracking directory (auto-generated)
├── src/mlProject/             # Core source code
│   ├── components/            # Data ingestion, transformation, etc.
│   ├── config/                # Configuration manager
│   ├── utils/                 # Utility functions
│   └── pipeline/              # Pipeline stages
│
├── templates/                 # HTML files for Flask
├── app.py                     # Flask application
├── main.py                    # Executes all pipeline stages
├── params.yaml                # Model hyperparameters
├── schema.yaml                # Data schema
├── dvc.yaml                   # DVC pipeline config
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

````

---

## ⚙️ Tech Stack

- Python
- ElasticNet (Scikit-learn)
- MLflow for experiment tracking
- DVC for data & model versioning
- Pandas, NumPy, Seaborn, Matplotlib
- Flask (for deployment)
- AWS EC2 (for cloud hosting)
- GitHub + DagsHub

---

## 🧪 Model Evaluation & MLflow

- Trained model: `ElasticNet Regression`
- Evaluation Metrics: RMSE, MAE, R2
- MLflow Tracking: [🔗 MLflow on DagsHub](https://dagshub.com/harshita0212/OenoFlow-smart-wine-prediction.mlflow)
- Tracks:
  - Parameters (`alpha`, `l1_ratio`)
  - Metrics (`rmse`, `mae`, `r2`)
  - Model artifacts

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/harshita0212/OenoFlow-smart-wine-prediction.git
cd OenoFlow-smart-wine-prediction
````

### 2. Set up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure MLflow Tracking (DagsHub)

Inside your script or `stage_05_model_evaluation.py`:

```python
import mlflow
import os

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/harshita0212/OenoFlow-smart-wine-prediction.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "your_username"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "your_token"

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
```

You can also store these credentials in a `.env` file and load using `python-dotenv`.

---

## ⚙️ Run the ML Pipeline

Run all stages sequentially using:

```bash
python main.py
```

Or run individual pipeline stages:

```bash
python src/mlProject/pipeline/stage_01_data_ingestion.py
python src/mlProject/pipeline/stage_02_data_validation.py
...
```

---

## 📊 MLflow UI (Optional Local)

If not using DagsHub and want to run MLflow UI locally:

```bash
mlflow ui
```

Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📈 DVC Usage

### Track Data with DVC

```bash
dvc init
dvc add data/winequality.csv
git add data/.gitignore winequality.csv.dvc
git commit -m "Track raw data with DVC"
```

### Run DVC Pipeline

```bash
dvc repro
```

---

## 🌐 Deployment on AWS EC2 with Flask

### Step-by-Step Guide

1. **Launch EC2 Instance** (Ubuntu preferred)
2. **SSH into EC2**

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

3. **Install Required Tools**

```bash
sudo apt update
sudo apt install python3-pip
sudo apt install python3-venv
```

4. **Clone Your Repo on EC2**

```bash
git clone https://github.com/harshita0212/OenoFlow-smart-wine-prediction.git
cd OenoFlow-smart-wine-prediction
```

5. **Create & Activate Virtual Env**

```bash
python3 -m venv venv
source venv/bin/activate
```

6. **Install Requirements**

```bash
pip install -r requirements.txt
```

7. **Run Flask App**

```bash
python app.py
```

8. **Configure Security Group in AWS**
   Allow **HTTP (port 80)** and **Custom TCP Rule (port 5000)** to access your app via browser.

---

## 🖥️ Flask Web App

You can use the web interface to:

* Input wine chemical features
* Get predicted wine quality

Hosted on: `http://<your-ec2-ip>:5000`

---

## 🙋‍♀️ Author

**Harshita Lalwani**

* Third-year Computer Science student, VIT
* [LinkedIn](https://www.linkedin.com/in/harshita-lalwani)
* [GitHub](https://github.com/harshita0212)

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Future Enhancements

* Add Dockerfile for containerized deployment
* Model Explainability with SHAP
* Interactive dashboards with Streamlit
* CI/CD with GitHub Actions
---
