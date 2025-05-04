# Weather Forecast Telegram Bot

A simple Telegram bot that provides weather forecasts for any city using the OpenWeatherMap API.

## Features

- `/start`: Welcomes the user and provides instructions.
- `/weather <city>`: Fetches and displays the current weather and temperature for the specified city.

## Requirements

- Python 3.9 or higher
- Telegram Bot Token (from [BotFather](https://core.telegram.org/bots#botfather))
- OpenWeatherMap API Key (from [OpenWeatherMap](https://openweathermap.org/api))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-forecast-bot.git
   cd weather-forecast-bot
   ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages: 
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Telegram Bot Token and OpenWeatherMap API Key:

    ```env
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    OPENWEATHERMAP_API_KEY=your_openweather_api_key
    ```


## Deployment
To deploy the bot, you can use platforms like Heroku, AWS, or PythonAnywhere. 
Refer to the deployment instructions in the project documentation.


## License
This project is licensed under the MIT License. See the LICENSE file for details.