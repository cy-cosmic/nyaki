import requests
from django.conf import settings
from django.core.cache import cache

PLACES_URL = "https://maps.googleapis.com/maps/api/place/details/json"
CACHE_KEY = "nyaki_afh_google_place_details"
CACHE_TTL = 60 * 60 * 6  # 6 hours


def fetch_place_details():
    params = {
        "place_id": settings.GOOGLE_PLACE_ID,
        "fields": "name,rating,reviews,user_ratings_total,formatted_phone_number,formatted_address",
        "key": settings.GOOGLE_PLACES_API_KEY,
    }

    response = requests.get(PLACES_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    print(response.json())

    if data.get("status") != "OK":
        raise Exception(f"Google Places error: {data.get('status')}")

    return data["result"]


def get_place_details_cached():
    cached = cache.get(CACHE_KEY)
    if cached:
        return cached

    data = fetch_place_details()
    cache.set(CACHE_KEY, data, CACHE_TTL)
    return data
