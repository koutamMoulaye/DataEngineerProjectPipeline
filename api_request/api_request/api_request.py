import requests

api_key = "64d3c85864eba2c31ca825f7810a7212"

api_url = f'http://api.weatherstack.com/current?access_key={api_key}&query=New York'


def fetch_data():
    print("fetching weather data from weatherstack API ...")
    try:

        response = requests.get(api_url)
        response.raise_for_status()
        print('API response received successfully. ')
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')
        raise


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-08-14 17:06', 'localtime_epoch': 1755191160, 'utc_offset': '-4.0'}, 'current': {'observation_time': '09:06 PM', 'temperature': 32, 'weather_code': 119, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0003_white_cloud.png'], 'weather_descriptions': ['Cloudy '], 'astro': {'sunrise': '06:06 AM', 'sunset': '07:55 PM', 'moonrise': '10:34 PM', 'moonset': '12:10 PM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 75}, 'air_quality': {'co': '725.2', 'no2': '103.045', 'o3': '99', 'so2': '18.685', 'pm2_5': '65.675', 'pm10': '66.045', 'us-epa-index': '4', 'gb-defra-index': '4'}, 'wind_speed': 10, 'wind_degree': 145, 'wind_dir': 'SE', 'pressure': 1014, 'precip': 0, 'humidity': 48, 'cloudcover': 0, 'feelslike': 34, 'uv_index': 1, 'visibility': 16, 'is_day': 'yes'}}