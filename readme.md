# 🍽 Restaurant API

A high-performance Restaurant API that allows users to find available restaurants based on their location, delivery radius, and operating hours.

## 🚀 Features
- Query restaurants by latitude & longitude.
- Optimized for low-latency responses.
- Uses CSV data updated every 6 hours.
- Runs in a Docker container.
- No authentication required.

## 🛠 Installation & Setup
- conda create --name restaurant-api python=3.10
- conda activate restaunrant-api
- pip install -r .\requirements.txt

### Prerequisites
- Python 3.9+
- Docker & Docker Compose

### Clone the Repository
```sh
git clone https://github.com/nidhiojha/restaurant-api.git
cd restaurant-api
