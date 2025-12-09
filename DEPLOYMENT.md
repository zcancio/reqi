# Deployment Guide - Vercel

This guide explains how to deploy the Reqi application to Vercel.

## Prerequisites

- A Vercel account (sign up at [vercel.com](https://vercel.com))
- Git repository (GitHub, GitLab, or Bitbucket)
- Vercel CLI (optional, for CLI deployment)

## Deployment Options

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push your code to a Git repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Import project on Vercel**
   - Go to [vercel.com/new](https://vercel.com/new)
   - Import your Git repository
   - Vercel will auto-detect Next.js

3. **Configure project settings**
   - **Root Directory**: Set to `frontend` (IMPORTANT: This tells Vercel where your Next.js app is)
   - **Framework Preset**: Next.js (should auto-detect)
   - **Build Command**: Leave as default (`npm run build`)
   - **Output Directory**: Leave as default (`.next`)
   - **Install Command**: Leave as default (`npm install`)

4. **Environment Variables** (if needed)
   - Add any environment variables in the Vercel dashboard
   - These will be available to both frontend and API routes

5. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete
   - Your app will be live at `https://your-project.vercel.app`

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Navigate to project root**
   ```bash
   cd /path/to/reqi
   ```

4. **Deploy from root (Vercel will use frontend directory)**
   ```bash
   vercel
   ```
   
   Follow the prompts:
   - Link to existing project or create new
   - **Set Root Directory**: Enter `frontend` when prompted
   - Confirm settings
   - Deploy

5. **For production deployment**
   ```bash
   vercel --prod
   ```

**Note**: When using CLI, you can also specify the root directory:
```bash
vercel --cwd frontend
```

## Project Structure for Vercel

Vercel will deploy the `frontend` directory as a Next.js application. The API routes are located in `frontend/api/` and will be automatically converted to serverless functions.

```
frontend/
├── app/                    # Next.js app directory
├── api/                    # Vercel serverless functions (Python)
│   ├── health.py
│   ├── index.py
│   └── v1/
│       └── requirements/
│           ├── index.py
│           └── [requirement_id].py
├── package.json
└── next.config.js
```

## API Routes

The API endpoints are available as serverless functions:
- `GET /api/` - Root API endpoint
- `GET /api/health` - Health check
- `GET /api/v1/requirements` - Get all requirements
- `POST /api/v1/requirements` - Create requirement
- `GET /api/v1/requirements/{id}` - Get specific requirement
- `PUT /api/v1/requirements/{id}` - Update requirement
- `DELETE /api/v1/requirements/{id}` - Delete requirement

## Environment Variables

If you need environment variables:

1. Go to your project settings on Vercel
2. Navigate to "Environment Variables"
3. Add variables for:
   - Production
   - Preview
   - Development

## Custom Domain

To add a custom domain:

1. Go to project settings on Vercel
2. Navigate to "Domains"
3. Add your domain
4. Follow DNS configuration instructions

## Continuous Deployment

Vercel automatically deploys on every push to your main branch:
- **Production**: Deploys from `main` branch
- **Preview**: Deploys from other branches and pull requests

## Troubleshooting

### Build Fails

- Check build logs in Vercel dashboard
- Ensure all dependencies are in `package.json`
- Verify Node.js version (Vercel uses Node 18.x by default)

### API Routes Not Working

- Ensure Python files are in `frontend/api/` directory
- Check function logs in Vercel dashboard
- Verify route paths match API calls

### CORS Issues

- API routes include CORS headers
- For custom domains, update CORS origins in API functions

## Local Development vs Production

- **Local**: Uses FastAPI backend on port 8000 (via proxy)
- **Production**: Uses Vercel serverless functions

The `next.config.js` automatically handles this difference based on `NODE_ENV`.

## Monitoring

- View function logs in Vercel dashboard
- Monitor performance and errors
- Set up alerts for critical issues

## Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Next.js Deployment](https://nextjs.org/docs/deployment)
- [Vercel Serverless Functions](https://vercel.com/docs/functions)

