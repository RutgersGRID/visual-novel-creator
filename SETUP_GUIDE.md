# Streamlit Template Setup Guide

This guide helps you set up and deploy a Streamlit application using the [RutgersGRID/streamlit-template](https://github.com/RutgersGRID/streamlit-template) on EmTech Cloud.

## Getting Started

### Prerequisites
- GitHub account
- Git installed locally
- Docker and Docker Compose installed for local testing
- Python 3.12 or compatible version
- uv package manager (`pip install uv`)

### Step 1: Clone the Template Repository
```bash
git clone https://github.com/RutgersGRID/streamlit-template.git
cd streamlit-template
```

## Project Structure
The template comes with a predefined structure:
```
streamlit-template/
├── .github/workflows/    # CI/CD configuration
├── docker/               # Docker configuration
├── src/                  # Application source code
│   └── streamlit_template/
│       ├── app.py        # Main application entry point
│       └── utils.py      # Utility functions
├── pyproject.toml        # Python dependencies and metadata
└── README.md             # Project documentation
```

## Development

### Setting Up the Development Environment
1. Create a virtual environment using uv:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

### Customizing Your Application
1. Edit the main application file at `src/streamlit_template/app.py`
2. Add utility functions in the `src/streamlit_template/utils.py` file
3. Update the package metadata in `pyproject.toml`

### Adding Dependencies
```bash
# Add a single package
uv add streamlit

# Add multiple packages
uv add pandas numpy matplotlib

# Add a package with specific version
uv add pandas==2.2.0

# Add a development dependency
uv add --dev pytest
```

### Testing Locally
Run your Streamlit application locally:
```bash
# Using uv (recommended)
uv run -m streamlit run src/streamlit_template/app.py

# Or directly with streamlit
streamlit run src/streamlit_template/app.py
```

## Docker Deployment

### Testing with Docker Compose
```bash
docker-compose -f docker/docker-compose.yml up
```
Visit http://localhost:8501 to see your application running in Docker.

### Building Docker Image
```bash
docker-compose -f docker/docker-compose.yml build
```

## Deploying to EmTech Cloud

Deployment is handled automatically by GitHub Actions. Simply push your code to trigger the deployment pipeline.

### Step 1: Push Your Code
Commit and push your changes to the main branch:
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Automatic Registration and Deployment
The GitHub Actions workflow will:
1. Automatically register your application
2. Build and tag the Docker image
3. Push the image to ECR
4. Deploy it to the ECS environment

The GitHub workflow uses the configuration defined in your repository's `.github/workflows/deploy.yml` file.

### Step 3: Monitor Deployment
You can monitor the deployment status in the "Actions" tab of your GitHub repository.

## Troubleshooting
- Check GitHub Actions workflow logs for build or deployment errors
- Ensure your code passes all tests locally before pushing
- Verify Docker builds successfully locally before deployment:
  ```bash
  docker-compose -f docker/docker-compose.yml build
  ```
- Contact your administrator if you encounter persistent deployment issues

## Best Practices
- Keep sensitive configuration in environment variables
- Document your code with comments and docstrings
- Follow the PEP 8 style guide for Python code (4 spaces, 79 chars/line)
- Use f-strings for string formatting
- Add type annotations for function parameters and returns
- Use try/except with specific exceptions for error handling
- Add dependencies to pyproject.toml with `uv add`
- Use uv for Python package management
- Optimize Streamlit performance using caching where appropriate
- AWS resources should use tags for cost tracking

## Security Best Practices
- Never commit secrets, credentials, or API keys to your repository
- Keep sensitive configuration in environment variables
- Use relative imports for your application modules
- Follow secure coding practices for data handling

## Getting Help
Contact your EmTech Cloud administrator for assistance with:
- Infrastructure configuration
- AWS permissions
- Deployment troubleshooting
