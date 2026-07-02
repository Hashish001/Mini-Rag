from fastapi import APIRouter, FastAPI
import os

base_router = APIRouter(
  prefix="/Hassan/v1",
  tags=["version 1"]
)

@base_router.get("/")
def welcome_message():
  app_name = os.getenv('APP_NAME')
  app_version = os.getenv('APP_VERSION')
  return{
    "message": "Hello Hassan Hashish in Fast API Router",
    "app_name": app_name,
    "app_version": app_version
  }