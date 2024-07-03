import { React, useEffect, useState } from "react";
import Temperature from "./componenets/Temperature";
import Highlights from "./componenets/Highlights";
// import React, { useState, } from 'react';
import DateInput from "./componenets/DateInput";
import HourlyUpdates from "./componenets/HourlyUpdates ";

function App() {
  const [date, setDate] = useState("2024-12-10"); // Example date
  const [weatherData, setWeatherData] = useState(null);

  useEffect(() => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ date: date }), // Sending date in the body
    };

    fetch("http://localhost:8000/fetch_weather", requestOptions)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Could not get data");
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        setWeatherData(data);
      })
      .catch((error) => {
        console.error("There was an error!", error);
      });
  }, [date]);

  return (
    <>
      <div className=" h-screen">
        <div className=" flex justify-center items-start">
          <div className="w-1/5 h-1/3 mt-40">
            <DateInput onDateChange={(newDate) => setDate(newDate)} />{" "}
            {/* Pass the callback */}
          </div>
          <div className="w-1/5 h-1/3 mt-40">
            {weatherData && (
              <Temperature
                stats={{
                  temp: weatherData.data.daily[2], // Adjust based on actual data structure
                  condition: weatherData.data.daily[15],
                  isDay: weatherData.data.daily[16] === "Yes", // Adjust logic based on actual data structure
                  location: "Kargil", // Placeholder, adjust as needed
                  sunrise: weatherData.data.daily[19], // Adjust index based on actual data structure
                  sunset: weatherData.data.daily[20], // Adjust index based on actual data structure
                  img: weatherData.data.daily[16],
                }}
              />
            )}
          </div>
          <div className="w-1/3 h-1/3 mt-40 p-10 grid grid-cols-2 gap-6">
            <h1 className="text-slate-200 text-2xl col-span-2">
              <span className="text-md font-semibold mx-1 text-blue-700">
                {date}
              </span>
              Highlights
            </h1>
            {weatherData && (
              <>
                <Highlights
                  stats={{
                    title: "Wind Speed",
                    value: weatherData.data.daily[8], // Adjust index based on actual data structure
                    unit: "mph",
                  }}
                />
                <Highlights
                  stats={{
                    title: "Humidity",
                    value: weatherData.data.daily[14],
                    unit: "%",
                  }}
                />
                <Highlights
                  stats={{
                    title: "Visibility",
                    value: weatherData.data.daily[12],
                    unit: "miles",
                  }}
                />
                <Highlights
                  stats={{
                    title: "Air Pressure",
                    value: weatherData.data.daily[7],
                    unit: "mb",
                  }}
                />
              </>
            )}
          </div>
        </div>
        <div className=" mt-10 p-5">
          {weatherData && (
            <HourlyUpdates hourlyData={weatherData.data.hourly} />
          )}
        </div>
      </div>
    </>
  );
}

export default App;
