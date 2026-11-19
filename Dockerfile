# Используем официальный легковесный образ Python (по методичке)
FROM python:3.11-slim

# Указываем рабочую папку внутри контейнера
WORKDIR /app

# Оптимизация для Python в контейнере (не писать .pyc и сразу выводить логи в консоль)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Шаг 1: Копируем только requirements.txt и ставим зависимости.
# Это нужно для кэширования: если код поменяется, зависимости не будут качаться заново!
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Шаг 2: Копируем исходный код нашего приложения
COPY cmd/ ./cmd/
COPY internal/ ./internal/

# Информируем, какой сетевой порт слушает приложение
EXPOSE 8080

# Команда запуска нашего сервера при старте контейнера
CMD ["python", "cmd/app/main.py"]
