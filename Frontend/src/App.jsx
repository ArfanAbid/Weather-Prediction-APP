import { React, useEffect, useState } from "react";
import Temperature from "./componenets/Temperature";
import Highlights from "./componenets/Highlights";
import DateInput from "./componenets/DateInput";
import HourlyUpdates from "./componenets/HourlyUpdates ";

function App() {
  const [date, setDate] = useState("2024-12-10"); // Example date
  const [weatherData, setWeatherData] = useState(null);
  const [ErrorMsg, setErrorMsg] = useState("")

  useEffect(() => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ date: date }), // Sending date in the body
    };

    fetch("http://localhost:8000/fetch_weather", requestOptions)
      .then((response) => {
        if (!response.ok) {
          console.log(response.detail)
          console.log("Error fetching data")
          alert("Error fetching data");
          // throw new Error("Could not get data");
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
      <div className="h-screen flex flex-col md:flex-row justify-center items-start">
        {/* <h1 className="text-slate-200">Weather APP Prediction</h1> */}
        <div className="w-full md:w-1/5 h-1/3 mt-10 md:mt-40 px-1">
          <DateInput onDateChange={(newDate) => setDate(newDate)} />
        </div>
        <div className="mt-10 md:mt-40">
          {weatherData && (
            <Temperature
              stats={{
                temp: weatherData.data.daily[2],
                condition: weatherData.data.daily[15],
                isDay: weatherData.data.daily[16] === "Yes",
                location: "Kargil",
                sunrise: weatherData.data.daily[19],
                sunset: weatherData.data.daily[20],
                img: weatherData.data.daily[16],
              }}
            />
          )}
        </div>
        <div className="w-full md:w-1/3 h-1/3 mt-10 md:mt-40 p-5">
          <h1 className="text-slate-200 text-xl md:text-2xl">
            <span className="text-md font-semibold mx-1 text-blue-700">
              {date}
            </span>
            Highlights
          </h1>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
            {weatherData && (
              <>
                <Highlights
                  stats={{
                    title: "Wind Speed",
                    value: weatherData.data.daily[8],
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
      </div>
      <div className="md:mt-5 p-5  mt-64">
        {weatherData && (
          <HourlyUpdates hourlyData={weatherData.data.hourly} />
        )}
      </div>
    </>
  );
}

export default App;