from app.services import get_available_restaurants

def test_get_available_restaurants(mocker):
    mocker.patch("app.utils.load_data", return_value=[
        {"id": 1, "latitude": 40.7128, "longitude": -74.0060, "availability_radius": 10, "open_hour": "08:00", "close_hour": "22:00"}
    ])
    result = get_available_restaurants(40.7128, -74.0060)
    assert 1 in result