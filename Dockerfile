# Multi-stage build for a lightweight and secure Docker image

# Stage 1: Build dependencies
FROM python:3.9-slim-bullseye AS builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Create a virtual environment and install dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production image
FROM python:3.9-slim-bullseye

# Set working directory
WORKDIR /app

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random

# Copy application code
COPY . .

# Non-root user for security
RUN addgroup --system appuser && \
    adduser --system --ingroup appuser appuser
USER appuser

# Expose port for Streamlit (default)
EXPOSE 8080

# Command to run the application
CMD ["streamlit", "run", "main.py"]