# Reqi - Requirements-Driven Web Application Generator

Reqi is a web application that enables you to define application requirements in a structured document, which is then used to automatically generate a fully functional web application.

## Overview

Reqi transforms requirements documents into working web applications. Simply define your application's requirements, data models, user interfaces, and business logic in a structured format, and Reqi will generate the corresponding web application code.

## Features

- **Requirements Document Definition**: Define your application requirements in a structured, human-readable format
- **Automatic Code Generation**: Generate complete web applications from requirements documents
- **Web-Based Interface**: Manage and edit requirements documents through an intuitive web interface
- **Multiple Framework Support**: Generate applications using popular web frameworks (planned)
- **Real-time Preview**: Preview generated applications before deployment (planned)

## How It Works

1. **Define Requirements**: Create a requirements document that specifies:
   - Data models and entities
   - User interface components
   - Business logic and workflows
   - API endpoints and data relationships
   - Authentication and authorization rules

2. **Generate Application**: Reqi processes your requirements document and generates:
   - Frontend components and pages
   - Backend API endpoints
   - Database schemas
   - Configuration files
   - Documentation

3. **Deploy**: Export or deploy the generated application to your preferred hosting platform

## Project Structure

```
reqi/
├── README.md
├── backend/              # FastAPI backend application
│   ├── main.py          # Main application file
│   ├── requirements.txt # Python dependencies
│   └── README.md        # Backend documentation
├── frontend/            # Next.js frontend application
│   ├── app/             # Next.js app directory
│   ├── package.json     # Node.js dependencies
│   └── README.md        # Frontend documentation
├── requirements/        # Example requirements documents
├── generator/           # Code generation engine (to be implemented)
└── output/             # Generated applications
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Node.js (v18 or higher)
- npm, yarn, or pnpm
- Git

### Installation

#### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Copy environment file
cp env.example .env
```

#### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install
# or
yarn install
# or
pnpm install
```

### Development

#### Start Backend Server

```bash
# From backend directory
cd backend
source venv/bin/activate  # Activate virtual environment if not already active
python main.py
# Or use uvicorn directly:
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend API will be available at:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

#### Start Frontend Server

```bash
# From frontend directory
cd frontend
npm run dev
# or
yarn dev
# or
pnpm dev
```

The frontend will be available at: http://localhost:3000

#### Running Both Servers

Open two terminal windows:
1. Terminal 1: Run the backend server (port 8000)
2. Terminal 2: Run the frontend server (port 3000)

## Requirements Document Format

Requirements documents are defined in a structured format (format TBD - JSON, YAML, or custom DSL).

Example structure:
```yaml
application:
  name: "My Application"
  description: "A sample application"
  
models:
  - name: User
    fields:
      - name: id
        type: string
      - name: email
        type: string
        required: true
  
pages:
  - name: Dashboard
    components:
      - type: list
        model: User
```

## Roadmap

- [ ] Requirements document parser
- [ ] Web-based requirements editor
- [ ] Code generation engine
- [ ] Frontend framework support (React, Vue, etc.)
- [ ] Backend framework support (Express, FastAPI, etc.)
- [ ] Database schema generation
- [ ] Authentication and authorization generation
- [ ] Real-time preview
- [ ] Export functionality
- [ ] Template system for custom generation rules

## Deployment

### Deploy to Vercel

The application is configured for easy deployment to Vercel. See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions.

**Quick Deploy:**

1. Push your code to a Git repository
2. Import the project on [Vercel](https://vercel.com/new)
3. Set **Root Directory** to `frontend`
4. Deploy!

The API routes in `frontend/api/` will automatically be converted to Vercel serverless functions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[License TBD]

## Contact

[Contact information TBD]

