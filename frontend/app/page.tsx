export default function Home() {
  return (
    <main style={{ padding: '2rem', minHeight: '100vh' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
        <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>
          Welcome to Reqi
        </h1>
        <p style={{ fontSize: '1.2rem', marginBottom: '2rem', color: '#666' }}>
          Requirements-Driven Web Application Generator
        </p>
        
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '1.5rem',
          marginTop: '2rem'
        }}>
          <div style={{
            padding: '1.5rem',
            border: '1px solid #ddd',
            borderRadius: '8px',
            backgroundColor: '#f9f9f9'
          }}>
            <h2 style={{ marginBottom: '1rem' }}>Define Requirements</h2>
            <p>Create structured requirements documents for your web applications.</p>
          </div>
          
          <div style={{
            padding: '1.5rem',
            border: '1px solid #ddd',
            borderRadius: '8px',
            backgroundColor: '#f9f9f9'
          }}>
            <h2 style={{ marginBottom: '1rem' }}>Generate Applications</h2>
            <p>Automatically generate complete web applications from your requirements.</p>
          </div>
          
          <div style={{
            padding: '1.5rem',
            border: '1px solid #ddd',
            borderRadius: '8px',
            backgroundColor: '#f9f9f9'
          }}>
            <h2 style={{ marginBottom: '1rem' }}>Deploy & Share</h2>
            <p>Export and deploy your generated applications anywhere.</p>
          </div>
        </div>
      </div>
    </main>
  )
}

