# Fizz Buzz REST API

## Features

- REST API using FastAPI
- Configurable FizzBuzz rules
- Input validation
- Health check endpoints 
- Request statistics
- Logging
- Unit tests
- Integration tests
- Docker support

## Installation
```bash
python -m venv venv
sourcee venv/bin/activate
pip install -r requirements.txt
```

## Run Tests
```
pytest
python -m pytest -v
```

## Docker
```bash
docker build -t fizzbuzz .
docker run -p 8000:8000 fizzbuzz
```

## API Endpoints
| Method | Endpoint | Description | 
|--------|----------|-------------|
| GET | `/` | Welcome endpoint |
| GET | `/fizzbuzz` | Generate Fizbuzz output |
| GET | `/health` | Health check |
| GET | `/statistics` | Most frequently requested parameter combination |  