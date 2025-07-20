```markdown
# 🍷 OenoFlow-smart-wine-prediction

**OenoFlow-smart-wine-prediction** is a complete end-to-end MLOps project that predicts the quality of wine using machine learning. It leverages data versioning, modular pipelines, CI/CD principles, model tracking with MLflow, and cloud deployment on AWS EC2.

---

## 🚀 Project Overview

This project demonstrates a production-level ML pipeline using:
- **Wine Quality Dataset** from UCI Machine Learning Repository.
- **MLOps best practices** including modular code structure, configuration management, logging, and exception handling.
- **MLflow** for experiment tracking and model registry.
- **AWS EC2** for model deployment.

---

```

OenoFlow-smart-wine-prediction/
│
├── .github/workflows/             # CI pipeline (GitHub Actions)
├── artifacts/                     # Generated artifacts like datasets, models, schema
├── config/                        # Configuration YAML files
├── src/mlProject/
│   ├── components/               # Feature engineering, model trainer etc.
│   ├── pipeline/                 # Stage-wise execution scripts
│   ├── config/configuration.py   # Configuration Manager
│   ├── utils/                    # Utility functions (logging, common ops)
│   ├── entity/                   # Data classes for configs
│   └── constants/                # Constants used in the pipeline
│
├── research/                     # EDA, notebooks, experimentation
├── templates/                    # HTML files (for flask app if needed)
├── main.py                       # Main pipeline trigger
├── app.py                        # Flask app for inference
├── Dockerfile                    # Docker configuration
├── requirements.txt              # Python dependencies
├── setup.py                      # Project metadata
└── README.md                     # Project documentation

````
---

## 🔧 Setup Instructions

### ⚙️ Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/OenoFlow-smart-wine-prediction.git
cd OenoFlow-smart-wine-prediction
````

### 🧪 Step 2: Create and Activate a Virtual Environment

```bash
conda create -n wine_env python=3.10 -y
conda activate wine_env
```

### 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧱 Pipeline Stages

Each pipeline stage is modular and defined inside the `src/mlProject/pipeline/` directory:

1. **Data Ingestion**
2. **Data Validation**
3. **Data Transformation**
4. **Model Training**
5. **Model Evaluation**

Run the complete pipeline:

```bash
python main.py
```

---

## 🎯 MLflow Tracking

Track your experiments:

```bash
mlflow ui
```

Then open browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ☁️ AWS EC2 Deployment

### ✅ Step 1: Launch EC2 Instance

* Choose **Ubuntu 20.04**
* Allow ports **22 (SSH)** and **5000 (Flask/MLflow)** in security group
* Use a key pair to SSH

### 🔐 Step 2: Connect to EC2

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

### 🐍 Step 3: Install Dependencies on EC2

```bash
sudo apt update && sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
git clone https://github.com/your-username/OenoFlow-smart-wine-prediction.git
cd OenoFlow-smart-wine-prediction
pip install -r requirements.txt
```

### 🚦 Step 4: Start MLflow Server (Optional)

```bash
mlflow ui --host 0.0.0.0 --port 5000
```

### 🌐 Step 5: Run Flask App for Inference

```bash
python app.py
```

Access the app on `http://<your-ec2-public-ip>:5000`

---

## 🐳 Optional: Docker Setup

Build and run with Docker:

```bash
docker build -t wine-predictor .
docker run -p 5000:5000 wine-predictor
```

---

## 📌 Future Enhancements

* Enable **CI/CD with GitHub Actions**
* Add **unit tests** with `pytest`
* Push **trained models to S3**
* Automate with **Terraform for AWS**

---

## 🤝 Contributing

Contributions and suggestions are welcome! Please fork the repo and submit a PR.

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Acknowledgements

* UCI Machine Learning Repository
* MLflow Team
* MLOps Zoomcamp Community

---

