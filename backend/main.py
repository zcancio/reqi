from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Reqi API",
    description="Requirements-Driven Web Application Generator API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to Reqi API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/api/v1/requirements")
async def get_requirements():
    """Get all requirements documents"""
    return {"requirements": []}


@app.post("/api/v1/requirements")
async def create_requirement():
    """Create a new requirements document"""
    return {"message": "Requirement created"}


@app.get("/api/v1/requirements/{requirement_id}")
async def get_requirement(requirement_id: str):
    """Get a specific requirements document"""
    return {"id": requirement_id, "data": {}}


@app.put("/api/v1/requirements/{requirement_id}")
async def update_requirement(requirement_id: str):
    """Update a requirements document"""
    return {"id": requirement_id, "message": "Requirement updated"}


@app.delete("/api/v1/requirements/{requirement_id}")
async def delete_requirement(requirement_id: str):
    """Delete a requirements document"""
    return {"id": requirement_id, "message": "Requirement deleted"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

