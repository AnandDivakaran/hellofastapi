# Use a small Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml /app/pyproject.toml
COPY main.py /app/main.py

# Install system deps required for building wheels (if any)
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*

# Install uv CLI into the image
RUN python -m pip install --no-cache-dir uv

# Create the project .venv and install dependencies into it
# uv venv creates .venv; uv pip then installs packages into that .venv
RUN uv venv \
 && uv pip install -r pyproject.toml

# Expose port
EXPOSE 80

# Run via uv so the command executes inside the project's .venv
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
