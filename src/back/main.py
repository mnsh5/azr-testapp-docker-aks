import random
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

@app.get("/")
async def root() -> dict:
  return {"Hello": "World"}

@router.get("/ping", summary="Get Ping", status_code=200)
async def get_ping() -> dict:
  return {"Ping": "🏓"}

@router.get("/icon", summary="Get all icons", response_class=PlainTextResponse, status_code=200)
async def get_icon() -> str:
  possible_icons = ["Kubernetes", "Mermaid", "Nessie", "Docker"]
  random_icon = random.choice(possible_icons)
  return random_icon

app.include_router(router, prefix=settings.API_V1_STR)
