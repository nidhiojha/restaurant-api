from pydantic import BaseModel

class Restaurant(BaseModel):
    id: int
    latitude: float
    longitude: float
    availability_radius: float
    open_hour: str
    close_hour: str