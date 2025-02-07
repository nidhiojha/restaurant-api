from fastapi import APIRouter
from app.services import get_available_restaurants

router = APIRouter()

@router.get("/restaurants")
def get_restaurants(latitude: float, longitude: float):
    return {"restaurants": get_available_restaurants(latitude, longitude)}