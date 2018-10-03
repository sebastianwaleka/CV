'''
Program will download weather from metaweather and show it according to given location.
'''

import urllib.request
import json

def weather(location):
    def get_location_id(location):
        with urllib.request.urlopen(
                f'https://www.metaweather.com/api/location/search/?query={location}') as weather_in_location:
            location_data = weather_in_location.read()
        location_data = json.loads(location_data)
        try:
            location_id = location_data[0]['woeid']
            return location_id
        except Exception:
            print('Nie znaleziono lokalizacji')
            exit(0)

    location_id = get_location_id(location)

    def get_weather_in_location(location_id):
        with urllib.request.urlopen(f'https://www.metaweather.com/api/location/{location_id}/') as weather:
            weather_data = weather.read()
        weather_data = json.loads(weather_data)
        return weather_data

    weather_data = get_weather_in_location(location_id)

    temp = float(weather_data['consolidated_weather'][0]['the_temp'])
    wind = float(weather_data['consolidated_weather'][0]['wind_speed'])
    humidity = int(weather_data['consolidated_weather'][0]['humidity'])
    air_pressure = float(weather_data['consolidated_weather'][0]['air_pressure'])

    output = f'''Weather in {location.capitalize()}:
    - temperature: {temp:.2f}°C
    - air pressure: {air_pressure:.3f} hPa
    - humidity: {humidity}%
    - wind speed: {wind:.2f} km/h'''

    return output
