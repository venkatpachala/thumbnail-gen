from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import background, cutout, compose

app = FastAPI(title="AI Thumbnail Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(background.router)
app.include_router(cutout.router)
app.include_router(compose.router)

app.mount("/uploads", StaticFiles(directory="backend/uploads"), name="uploads")


@app.get("/")
async def root():
    return {"message": "Thumbnail generator API"}
