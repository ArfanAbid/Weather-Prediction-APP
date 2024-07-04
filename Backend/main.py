from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:5173", "http://localhost:5173/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WeatherData(BaseModel):
    date: str

@app.post("/fetch_weather")
async def fetch_weather(data: WeatherData):
    try:
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        
        query_daily = '''
        SELECT * FROM forecast_day
        WHERE date = ?
        '''
        cursor.execute(query_daily, (data.date,))
        daily_result = cursor.fetchone()
        
        if not daily_result:
            raise HTTPException(status_code=404, detail="No daily weather data found for the given date")
        
        query_hourly = '''
        SELECT * FROM hourly_forecast
        WHERE substr(time, 1, 10) = ?
        '''
        cursor.execute(query_hourly, (data.date,))
        hourly_results = cursor.fetchall()
        
        if hourly_results:
            combined_data = {
                "daily": daily_result,
                "hourly": hourly_results
            }
            return {"message": "Weather data found", "data": combined_data}
        else:
            raise HTTPException(status_code=404, detail="No hourly weather data found for the given date")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    finally:
        conn.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
