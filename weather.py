import requests
from datetime import datetime, timedelta

parameters = {
    'lat': 28.535517,
    'lng': 77.391029,
    'formatted': 0,  # ISO 8601 format
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()

sunrise_utc = datetime.fromisoformat(data['results']['sunrise'])
sunset_utc = datetime.fromisoformat(data['results']['sunset'])

# Convert UTC to IST by adding 5 hours and 30 minutes
ist_offset = timedelta(hours=5, minutes=30)
sunrise_ist = sunrise_utc + ist_offset
sunset_ist = sunset_utc + ist_offset

# Current time in IST
time_now_ist = datetime.utcnow() + ist_offset

print("Sunrise Hour (IST):", sunrise_ist.hour)
print("Sunset Hour (IST):", sunset_ist.hour)
print("Current Hour (IST):", time_now_ist.hour)
