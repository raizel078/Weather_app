from apicode import API_kEY
import requests


def get_weather_by_city(search_input):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    city = str(search_input).strip().lower()
    if not city:
        city = 'Riyadh'
    params ={
        'q':city,
        'appid':API_kEY,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError:
        return f'error could not find the city{city}'
    except requests.exceptions.RequestException as e:
        return f'an unexpected error occurred {e}'
