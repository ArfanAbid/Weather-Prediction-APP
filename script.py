import requests
import sqlite3
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from time import sleep

load_dotenv()
# Define the API endpoint and parameters
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
LOCATION = os.getenv("LOCATION")

# Set specific start and end dates
start_date = datetime(2024, 7, 15)
end_date = datetime(2025, 4, 27)

# Generate dates range
dates_range = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1)]

# Function to send request with retries
def get_weather_data(url, params, retries=5, backoff_factor=0.3):
    for retry in range(retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error {response.status_code}: {response.reason}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            sleep(backoff_factor * (2 ** retry))  # Exponential backoff
    return None

for date in dates_range:
    params = {
        'key': api_key,
        'q': location,
        'dt': date
    }

    # Get weather data
    weather_data = get_weather_data(url, params)

    if weather_data:
        # Connect to SQLite database
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()

        # Create tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS location (
                name TEXT,
                region TEXT,
                country TEXT,
                lat REAL,
                lon REAL,
                tz_id TEXT,
                localtime_epoch INTEGER,
                localtime TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS forecast_day (
                date TEXT,
                date_epoch INTEGER,
                maxtemp_c REAL,
                maxtemp_f REAL,
                mintemp_c REAL,
                mintemp_f REAL,
                avgtemp_c REAL,
                avgtemp_f REAL,
                maxwind_mph REAL,
                maxwind_kph REAL,
                totalprecip_mm REAL,
                totalprecip_in REAL,
                avgvis_km REAL,
                avgvis_miles REAL,
                avghumidity REAL,
                condition_text TEXT,
                condition_icon TEXT,
                condition_code INTEGER,
                uv REAL,
                sunrise TEXT,
                sunset TEXT,
                moonrise TEXT,
                moonset TEXT,
                moon_phase TEXT,
                moon_illumination INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hourly_forecast (
                time_epoch INTEGER,
                time TEXT,
                temp_c REAL,
                temp_f REAL,
                is_day INTEGER,
                condition_text TEXT,
                condition_icon TEXT,
                condition_code INTEGER,
                wind_mph REAL,
                wind_kph REAL,
                wind_degree INTEGER,
                wind_dir TEXT,
                pressure_mb REAL,
                pressure_in REAL,
                precip_mm REAL,
                precip_in REAL,
                humidity INTEGER,
                cloud INTEGER,
                feelslike_c REAL,
                feelslike_f REAL,
                windchill_c REAL,
                windchill_f REAL,
                heatindex_c REAL,
                heatindex_f REAL,
                dewpoint_c REAL,
                dewpoint_f REAL,
                will_it_rain INTEGER,
                chance_of_rain INTEGER,
                will_it_snow INTEGER,
                chance_of_snow INTEGER,
                vis_km REAL,
                vis_miles REAL,
                gust_mph REAL,
                gust_kph REAL,
                uv REAL
            )
        ''')

        # Insert location data into 'location' table
        location_data = weather_data['location']
        cursor.execute('''
            INSERT INTO location (name, region, country, lat, lon, tz_id, localtime_epoch, localtime)
            VALUES (?,?,?,?,?,?,?,?)
        ''', (
            location_data['name'], 
            location_data['region'], 
            location_data['country'], 
            location_data['lat'], 
            location_data['lon'], 
            location_data['tz_id'], 
            location_data['localtime_epoch'], 
            location_data['localtime']
        ))

        # Insert forecast day data into 'forecast_day' table
        forecast_day_data = weather_data['forecast']['forecastday'][0]
        day_data = forecast_day_data['day']
        astro_data = forecast_day_data['astro']
        cursor.execute('''
            INSERT INTO forecast_day (
                date, date_epoch, maxtemp_c, maxtemp_f, mintemp_c, mintemp_f, avgtemp_c, avgtemp_f,
                maxwind_mph, maxwind_kph, totalprecip_mm, totalprecip_in, avgvis_km, avgvis_miles,
                avghumidity, condition_text, condition_icon, condition_code, uv, sunrise, sunset,
                moonrise, moonset, moon_phase, moon_illumination
            )
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', (
            forecast_day_data['date'], 
            forecast_day_data['date_epoch'], 
            day_data['maxtemp_c'], 
            day_data['maxtemp_f'], 
            day_data['mintemp_c'], 
            day_data['mintemp_f'], 
            day_data['avgtemp_c'], 
            day_data['avgtemp_f'], 
            day_data['maxwind_mph'], 
            day_data['maxwind_kph'], 
            day_data['totalprecip_mm'], 
            day_data['totalprecip_in'], 
            day_data['avgvis_km'], 
            day_data['avgvis_miles'], 
            day_data['avghumidity'], 
            day_data['condition']['text'], 
            day_data['condition']['icon'], 
            day_data['condition']['code'], 
            day_data['uv'], 
            astro_data['sunrise'], 
            astro_data['sunset'], 
            astro_data['moonrise'], 
            astro_data['moonset'], 
            astro_data['moon_phase'], 
            astro_data['moon_illumination']
        ))

        for hour_data in forecast_day_data['hour']:
            cursor.execute('''
                INSERT INTO hourly_forecast (
                    time_epoch, time, temp_c, temp_f, is_day, condition_text, condition_icon, condition_code,
                    wind_mph, wind_kph, wind_degree, wind_dir, pressure_mb, pressure_in, precip_mm, precip_in,
                    humidity, cloud, feelslike_c, feelslike_f, windchill_c, windchill_f, heatindex_c, heatindex_f,
                    dewpoint_c, dewpoint_f, will_it_rain, chance_of_rain, will_it_snow, chance_of_snow, vis_km,
                    vis_miles, gust_mph, gust_kph, uv 
                ) 
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (
                hour_data['time_epoch'],
                hour_data['time'],
                hour_data['temp_c'],
                hour_data['temp_f'],
                hour_data['is_day'],
                hour_data['condition']['text'],
                hour_data['condition']['icon'],
                hour_data['condition']['code'],
                hour_data['wind_mph'],
                hour_data['wind_kph'],
                hour_data['wind_degree'],
                hour_data['wind_dir'],
                hour_data['pressure_mb'],
                hour_data['pressure_in'],
                hour_data['precip_mm'],
                hour_data['precip_in'],
                hour_data['humidity'],
                hour_data['cloud'],
                hour_data['feelslike_c'],
                hour_data['feelslike_f'],
                hour_data['windchill_c'],
                hour_data['windchill_f'],
                hour_data['heatindex_c'],
                hour_data['heatindex_f'],
                hour_data['dewpoint_c'],
                hour_data['dewpoint_f'],
                hour_data['will_it_rain'],
                hour_data['chance_of_rain'],
                hour_data['will_it_snow'],
                hour_data['chance_of_snow'],
                hour_data['vis_km'],
                hour_data['vis_miles'],
                hour_data['gust_mph'],
                hour_data['gust_kph'],
                hour_data['uv']
            ))
        # Commit changes and close connection
        conn.commit()
        conn.close()

        print(f"Data saved successfully to SQLite database for {date}")
    else:
        print(f'Error fetching data for {date}')

