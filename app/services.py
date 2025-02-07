from geopy.distance import geodesic
from datetime import datetime
from app.utils import load_restaurant_data

def fetch_valid_restaurants(latitude: float, longitude: float):
    restaurant_data = load_restaurant_data()
    restaurant_data.fillna({'latitude': 0.0, 'longitude': 0.0}, inplace=True)

    user_location = (latitude, longitude)
    now = datetime.utcnow().time()

    valid_restaurants = []
    for _, row in restaurant_data.iterrows():
        store_loc = (row['latitude'], row['longitude'])
        if geodesic(user_location, store_loc).km <= row['availability_radius']:
            open_time = datetime.strptime(row['open_hour'], "%H:%M:%S").time()
            close_time = datetime.strptime(row['close_hour'], "%H:%M:%S").time()
            if open_time <= now <= close_time:
                valid_restaurants.append(row['id'])

    return valid_restaurants
