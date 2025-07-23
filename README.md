
```markdown
```

# 🍷 OenoFlow – Smart Wine Quality Prediction

OenoFlow is a complete end-to-end Machine Learning pipeline for predicting wine quality using ML models. It is built using Python, MLflow, DVC for versioning, and deployed with Flask on an AWS EC2 instance.

---
<img width="1024" height="1024" alt="ChatGPT Image Jul 23, 2025, 11_18_38 AM" src="https://github.com/user-attachments/assets/4f59c74d-f5f7-436c-a6ba-7f3979325a32" />


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

```
## ⚙️ Tech Stack
```
- Python
- ElasticNet (Scikit-learn)
- MLflow for experiment tracking
- DVC for data & model versioning
- Pandas, NumPy, Seaborn, Matplotlib
- Flask (for deployment)
- AWS EC2 (for cloud hosting)
- GitHub + DagsHub

---
```
## 🧪 Model Evaluation & MLflow

- Trained model: `ElasticNet Regression`
- Evaluation Metrics: RMSE, MAE, R2
- MLflow Tracking: [🔗 MLflow on DagsHub](https://dagshub.com/harshita0212/OenoFlow-smart-wine-prediction.mlflow)
- Tracks:
  - Parameters (`alpha`, `l1_ratio`)
  - Metrics (`rmse`, `mae`, `r2`)
  - Model artifacts

---
```
## 📦 Installation & Setup
```
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

- **Create ECR repo to store/save docker image**
728301184963.dkr.ecr.eu-north-1.amazonaws.com/mlprojectharshita

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
# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=entbappy \
MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


