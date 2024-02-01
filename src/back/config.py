from typing import List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  API_V1_STR: str = "/api/v1"
  BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:5173"
  ]
  PROJECT_NAME: str = "azr-testapp-docker-aks"

  class Config:
        case_sensitive = True



settings = Settings()
