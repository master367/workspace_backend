#!/bin/sh
set -e

# Выполнение миграций при старте
echo "Applying database migrations..."
alembic upgrade head

# Создание начального админа, если его нет
echo "Seeding initial data..."
python scripts/seed_admin.py

# Запуск приложения
echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
