from geopy.distance import geodesic
from datetime import datetime
from app.utils import load_data

def get_available_restaurants(latitude: float, longitude: float):
    data = load_data()
    print("data type........", type(data))
    # OR
    data.fillna({'latitude': 0.0, 'longitude': 0.0}, inplace=True)  # Replace NaN with default values

    user_location = (latitude, longitude)
    now = datetime.utcnow().time()
    print("lat..:", data["latitude"])
    print("long..:", data["longitude"])

    valid_restaurants = []
    for _, row in data.iterrows():
        store_location = (row['latitude'], row['longitude'])
        if geodesic(user_location, store_location).km <= row['availability_radius']:
            open_time = datetime.strptime(row['open_hour'], "%H:%M:%S").time()
            close_time = datetime.strptime(row['close_hour'], "%H:%M:%S").time()
            if open_time <= now <= close_time:
                valid_restaurants.append(row['id'])

    return valid_restaurants
