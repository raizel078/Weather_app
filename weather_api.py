from apicode import API_kEY
import requests

base_url = 'https://api.openweathermap.org/data/2.5/weather'
api = API_kEY
city = 'Riyadh'

full_url = f'{base_url}?q={city}&appid={api}&units=metric'