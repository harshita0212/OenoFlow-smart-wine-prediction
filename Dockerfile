FROM python:3.10-slim-bookworm
RUN apt-get update && apt-get install -y awscli

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]