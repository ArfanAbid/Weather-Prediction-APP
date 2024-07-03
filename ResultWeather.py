import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

# Define the date to search for
date_to_search = '2024-12-10'

# Query to fetch data for the specified date
cursor.execute('''
    SELECT *
    FROM forecast_day
    WHERE date = ?
''', (date_to_search,))

# Fetch the results
forecast_data = cursor.fetchone()

# Print the details
if forecast_data:
    print(f"Details for {date_to_search}:")
    print("---------------------------------------------")
    print(f"Date: {forecast_data[0]}")
    print(f"Max Temperature: {forecast_data[2]}°C / {forecast_data[3]}°F")
    print(f"Min Temperature: {forecast_data[4]}°C / {forecast_data[5]}°F")
    print(f"Avg Temperature: {forecast_data[6]}°C / {forecast_data[7]}°F")
    print(f"Max Wind Speed: {forecast_data[8]} mph / {forecast_data[9]} kph")
    print(f"Total Precipitation: {forecast_data[10]} mm / {forecast_data[11]} in")
    print(f"Avg Visibility: {forecast_data[12]} km / {forecast_data[13]} miles")
    print(f"Avg Humidity: {forecast_data[14]}%")
    print(f"Condition: {forecast_data[15]}")
    print(f"UV Index: {forecast_data[18]}")
    print(f"Sunrise: {forecast_data[19]}")
    print(f"Sunset: {forecast_data[20]}")
    print(f"Moonrise: {forecast_data[21]}")
    print(f"Moonset: {forecast_data[22]}")
    print(f"Moon Phase: {forecast_data[23]}")
    print(f"Moon Illumination: {forecast_data[24]}%")
    print("---------------------------------------------")
else:
    print(f"No data found for {date_to_search}")

# Close connection
conn.close()