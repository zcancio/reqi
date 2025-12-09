// API route to check backend health
export async function GET() {
  try {
    const response = await fetch('http://localhost:8000/health', {
      cache: 'no-store',
    });
    const data = await response.json();
    return Response.json(data);
  } catch (error) {
    return Response.json(
      { status: 'unhealthy', error: 'Backend server not reachable' },
      { status: 503 }
    );
  }
}

