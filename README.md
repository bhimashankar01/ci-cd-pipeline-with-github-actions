# CI/CD Pipeline with GitHub Actions

A simple FastAPI application demonstrating CI/CD pipeline setup with GitHub Actions.

## Features

- FastAPI REST API with basic endpoints
- Automated testing with pytest
- GitHub Actions CI pipeline

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn src.main:app --reload
```

## Running Tests

```bash
pytest tests/ -v
```

## API Endpoints

- `GET /` - Returns a greeting message
- `GET /add?a=10&b=20` - Adds two numbers and returns the result