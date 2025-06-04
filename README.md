# Streamlit Template

A modern Streamlit project template for deploying applications on EmTech Cloud.

## About This Template

This template provides a complete foundation for building and deploying Streamlit applications using the [RutgersGRID/streamlit-template](https://github.com/RutgersGRID/streamlit-template). It includes Docker integration, AWS deployment via GitHub Actions, and best practices for Python development.

## Getting Started

### Prerequisites
- GitHub account
- Git installed locally
- Docker and Docker Compose installed for local testing
- Python 3.12 or higher
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

2. Install dependencies:
   ```bash
   uv sync
   ```

### Customizing Your Application
1. Edit the main application file at `src/streamlit_template/app.py`
2. Add utility functions in `src/streamlit_template/utils.py`
3. Update the package metadata in `pyproject.toml`

### Testing Locally
Run your Streamlit application:
```bash
streamlit run src/streamlit_template/app.py
```

Or use uv to run:
```bash
uv run -m streamlit run src/streamlit_template/app.py
```

## Docker Deployment

### Testing with Docker Compose
```bash
docker-compose -f docker/docker-compose.yml up
```
Visit http://localhost:8501 to see your application running in Docker.

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
- Follow the style guide in CLAUDE.md for consistent code quality
- Add type annotations for function parameters and returns
- Use try/except with specific exceptions for error handling
- Add dependencies to pyproject.toml
- Use uv for Python package management
- Optimize Streamlit performance using caching where appropriate

## Dependency Management with uv

This project uses the [uv](https://github.com/astral-sh/uv) package manager for faster, more reliable Python dependency management.

### Adding Dependencies
```bash
# Add a package
uv add streamlit

# Add multiple packages
uv add pandas numpy matplotlib

# Add a package with specific version
uv add pandas==2.2.0

# Add a development dependency
uv add --dev pytest
```

### Syncing Dependencies
```bash
uv sync
```

## Development Workflow

For detailed information on the development workflow, see [WORKFLOW.md](WORKFLOW.md).

## License

[MIT](LICENSE)
