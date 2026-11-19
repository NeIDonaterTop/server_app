import sys
import os

# Добавляем корень проекта в пути импорта
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import uvicorn
from fastapi import FastAPI
from internal.config.config import config
from internal.controller.health import router as health_router

# Создаем приложение FastAPI
app = FastAPI(
    title=config.app_name,
    version=config.version,
    description="Сквозной проект UptimePulse (Лабораторная работа №3)"
)

# Подключаем роутер проверки здоровья
app.include_router(health_router)

if __name__ == "__main__":
    print(f"Запуск {config.app_name} на http://localhost:{config.http_port} (Окружение: {config.app_env})")
    uvicorn.run(app, host="0.0.0.0", port=config.http_port)
