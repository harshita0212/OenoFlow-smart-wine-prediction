
```markdown
# 🍷 OenoFlow-smart-wine-prediction

**OenoFlow-smart-wine-prediction** is a complete end-to-end MLOps project that predicts the quality of wine using machine learning.

---

## 🚀 Project Overview

This project demonstrates a production-level ML pipeline using:
- **Wine Quality Dataset** from UCI Machine Learning Repository.
- **MLOps best practices** including modular code structure, configuration management, logging, and exception handling.
- **MLflow** for experiment tracking and model registry.
- **AWS EC2** for model deployment.

---

## 📁 Project Structure

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

## 🛠️ Setup Instructions

### ✨ Step 1: Clone the Repository

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

## 🔁 Run the Pipeline

```bash
python main.py
```

This will execute all stages: ingestion, validation, transformation, training, and evaluation.

---

## 📊 MLflow Tracking

```bash
mlflow ui
```

Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ☁️ AWS EC2 Deployment

### ✅ 1. Launch EC2

* AMI: Ubuntu 20.04
* Open ports **22 (SSH)** and **5000 (Flask/MLflow)** in the security group

### 🔐 2. Connect to Instance

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

### 📦 3. Setup Project on EC2

```bash
sudo apt update && sudo apt install python3-pip python3-venv -y
git clone https://github.com/your-username/OenoFlow-smart-wine-prediction.git
cd OenoFlow-smart-wine-prediction
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🚦 4. Run Flask App

```bash
python app.py
```

Go to `http://<your-ec2-public-ip>:5000`

---

## 🐳 Docker (Optional)

```bash
docker build -t wine-predictor .
docker run -p 5000:5000 wine-predictor
```

---

## 🧠 Future Enhancements

* Add **unit tests** with `pytest`
* Push trained models to **AWS S3**
* Add **CI/CD pipeline**
* Automate AWS deployment using **Terraform**

---

## 🤝 Contributing

Contributions welcome! Please fork and raise a pull request.

---

## 📜 License

Licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* UCI ML Repository
* MLflow team
* MLOps Zoomcamp inspiration

---


