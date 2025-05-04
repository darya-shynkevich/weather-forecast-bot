from pydantic import BaseSettings


class Config(BaseSettings):
    telegram_bot_token: str
    openweathermap_api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
