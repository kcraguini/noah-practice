# Phishing Program (Gmail Fetch Prototype)

Small Python script that authenticates with Gmail and fetches recent inbox messages.

## Requirements

- Python 3.10+
- Docker Desktop (for containerized run)
- A Google OAuth `credentials.json` file (Desktop app client)

## Local Run (without Docker)

1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Place `credentials.json` in this folder.
3. Run:
   ```bash
   python phishing-detector.py
   ```

## Docker Run

1. Start Docker Desktop first (important).
2. Build image:
   ```bash
   docker build -t phishing-detector .
   ```
3. Run with your OAuth file mounted into the container:
   ```bash
   docker run --rm -it \
     -v "$PWD/credentials.json:/app/credentials.json:ro" \
     phishing-detector
   ```

## Why your Docker command failed

You got:

- `failed to connect to the docker API ... docker.sock ... no such file or directory`

That means the Docker daemon was not running. On macOS, open Docker Desktop and wait until it says Docker is running, then retry the build command.

## Optional: BuildKit warning

You also saw a deprecation warning about the legacy builder. It is only a warning. You can still build, but you can switch to BuildKit later by installing/using buildx.
