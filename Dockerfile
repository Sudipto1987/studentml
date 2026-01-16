# Change from 3.8 to 3.9 (or 3.10) to support Scikit-Learn 1.5.2
FROM python:3.9-slim-bullseye

WORKDIR /app
COPY . /app

# The build tools are still needed for CatBoost/XGBoost
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

CMD ["python3", "app.py"]