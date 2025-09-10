# AI Thumbnail Generator

A full-stack web application that creates YouTube-style thumbnails using AI.

## Features
- Generate background images from a text prompt via Stable Diffusion
- Remove background from uploaded photos with Rembg
- Compose background, cutout photo and overlay text into a 1280×720 thumbnail
- Download or preview the resulting image

## Project Structure
```
backend/   # FastAPI service
frontend/  # Next.js client
```

## Backend
Run locally:
```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

## Frontend
Install dependencies and start development server:
```bash
cd frontend
npm install
npm run dev
```
Set `NEXT_PUBLIC_API_URL` to the deployed FastAPI URL.

## Deployment
- **Backend:** Deploy the `backend` folder on Render or Railway using the provided `Dockerfile`.
- **Frontend:** Deploy the `frontend` folder to Vercel. Configure the environment variable `NEXT_PUBLIC_API_URL` with your backend URL.

## API Endpoints
- `POST /generate-background` – body: `{ "prompt": "text" }`
- `POST /cutout-photo` – form-data with image file
- `POST /compose-thumbnail` – body: `{ "background": "path", "cutout": "path", "text": "My title" }`

Generated files are stored in `backend/uploads/` and served at `/uploads/`.
