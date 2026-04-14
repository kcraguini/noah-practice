FROM python:3.11-slim as base

RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir \
    google-auth-oauthlib \
    google-auth \
    google-api-python-client

# Copy the application code
COPY phishing-detector.py .
COPY credentials.json . 2>/dev/null || true

# Set the default command
CMD ["python", "phishing-detector.py"]
