FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv for faster Python package installation
RUN pip install --no-cache-dir uv

# Copy only the dependency-related files first
COPY pyproject.toml README.md ./

# Install dependencies
RUN uv sync

# Copy the application code
# First, copy the source code separately for better layer caching
COPY src ./src/
# Then copy remaining files
COPY . .

# Expose port for Streamlit
EXPOSE 8501

# Set the PYTHONPATH to include src directory
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Healthcheck to ensure application is running
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Start Streamlit app using uv run
CMD ["uv", "run", "-m", "streamlit", "run", "src/streamlit_template/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
