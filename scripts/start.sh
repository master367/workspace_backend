#!/bin/sh
set -e

# Выполнение миграций при старте
echo "Applying database migrations..."
alembic upgrade head

# Запуск приложения
echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
