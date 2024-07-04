# Weather-Prediction-APP

# Weather Prediction App

This is a weather prediction application that fetches future weather data from a weather API and stores it in a database. The backend is built with FastAPI and allows fetching daily and hourly weather updates. The frontend is developed using React and Tailwind CSS.

## Features

- Fetch future weather data using a weather API.
- Store fetched weather data in a database.
- Provide daily and hourly weather updates via an API.
- Responsive user interface built with React and Tailwind CSS.

## Technologies Used

- **Backend:** FastAPI, Python
- **Frontend:** React, Tailwind CSS
- **Database:** SQLlite3 (or specify your database)

## Installation

### Prerequisites

- Python 3.8+
- Node.js and npm
- SQLlite (or your chosen database)

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ArfanAbid/Weather-Prediction-APP.git
   cd weather-prediction-app/backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for the weather API key in a `.env` file:

   ```env
   API_KEY=your_weather_api_key
   API_URL=your_weather_api_url
   ```

5. Run the script to fetch and store future weather data:

   ```bash
   python script.py
   ```

6. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd ../frontend
   ```

2. Install the dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## Usage

1. Run the backend server:

   ```bash
   uvicorn main:app --reload
   ```

2. Run the frontend development server:

   ```bash
   npm run dev
   ```

3. Open your browser and go to `http://localhost:5173/` to see the application in action.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any features, bug fixes, or enhancements.
