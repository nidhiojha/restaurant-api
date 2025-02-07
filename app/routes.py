from fastapi import APIRouter
from app.services import fetch_valid_restaurants

router = APIRouter()

@router.get("/restaurants")
def get_restaurants(latitude: float, longitude: float):
    return {"restaurants": fetch_valid_restaurants(latitude, longitude)}