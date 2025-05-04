import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import Config


class WeatherForecastBot:
    def __init__(self):
        config = Config()

        self._weather_api_key = config.openweathermap_api_key
        self._telegram_bot_token = config.telegram_bot_token

        self._application = (
            Application.builder().token(self._telegram_bot_token).build()
        )

        self._application.add_handler(CommandHandler("start", self.start))
        self._application.add_handler(CommandHandler("weather", self.weather))

    async def get_weather(self, city: str) -> str:
        url = (
            f"http://api.openweathermap.org/data/2.5/"
            f"weather?q={city}&appid={self._weather_api_key}&units=metric"
        )

        try:
            response = requests.get(url)

            if response.status_code == 404:
                return "City not found. Please try again."
            elif response.status_code != 200:
                return f"Error: Unable to fetch weather data ({response})."

            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
        except Exception as e:
            return f"Error fetching weather data: {e}"

        return f"Weather in {city}: {weather}, Temperature: {temp}°C"

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
            "Welcome to the Weather Bot! Use /weather <city> to get the forecast."
        )

    async def weather(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if len(context.args) == 0:
            await update.message.reply_text(
                "Please provide a city name. Usage: /weather <city>"
            )
            return

        city = " ".join(context.args)
        forecast = await self.get_weather(city)
        await update.message.reply_text(forecast)

    def run(self):
        self._application.run_polling()


if __name__ == "__main__":
    bot = WeatherForecastBot()
    bot.run()
