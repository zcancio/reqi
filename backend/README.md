# Reqi Backend

FastAPI backend for the Reqi application.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy environment file:
```bash
cp .env.example .env
```

4. Run the development server:
```bash
python main.py
# Or use uvicorn directly:
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/v1/requirements` - Get all requirements
- `POST /api/v1/requirements` - Create a requirement
- `GET /api/v1/requirements/{id}` - Get a specific requirement
- `PUT /api/v1/requirements/{id}` - Update a requirement
- `DELETE /api/v1/requirements/{id}` - Delete a requirement

