import os
from dotenv import load_dotenv

# Загружаем переменные из локального файла .env
load_dotenv()

class Config:
    app_name: str = os.getenv("APP_NAME", "UptimePulse API")
    app_env: str = os.getenv("APP_ENV", "development")
    version: str = os.getenv("VERSION", "1.0.0")
    http_port: int = int(os.getenv("HTTP_PORT", "8080"))

# Создаем один экземпляр конфигурации для всего приложения
config = Config()
