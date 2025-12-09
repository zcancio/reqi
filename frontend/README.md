# Reqi Frontend

Next.js frontend for the Reqi application.

## Setup

1. Install dependencies:
```bash
npm install
# or
yarn install
# or
pnpm install
```

2. Run the development server:
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
frontend/
├── app/              # Next.js app directory
│   ├── layout.tsx   # Root layout
│   ├── page.tsx     # Home page
│   └── globals.css  # Global styles
├── public/          # Static assets
└── components/      # React components (to be created)
```

## API Integration

The frontend is configured to proxy API requests to the backend running on `http://localhost:8000`. This is configured in `next.config.js`.

