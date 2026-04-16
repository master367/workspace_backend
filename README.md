# Internal Team Workspace Backend

## 🚀 Быстрый запуск

Самый простой способ запустить проект — использовать **Docker Compose**.

1. **Клонируйте репозиторий** и перейдите в папку проекта.
2. **Настройте окружение**:
   Скопируйте пример файла настроек:
   ```bash
   cp .env.example .env
   ```
   *(Для Windows в PowerShell: `cp .env.example .env`, в CMD: `copy .env.example .env`)*.
3. **Запустите проект**:
   ```bash
   docker-compose up --build -d
   ```
   Эта команда соберет образ бекенда, запустит базу данных и автоматически применит все миграции.
4. **Проверьте работу**:
   Откройте в браузере: [http://localhost:8000/docs](http://localhost:8000/docs)
5. **Войдите под администратором**:
   - Нажмите кнопку **Authorize** в правом верхнем углу Swagger.
   - Введите данные:
     - **Username**: `admin@example.com`
     - **Password**: `adminpassword123`

---

## О проекте
Backend-система для внутреннего рабочего пространства одной команды/компании. 

## Стек технологий
- **Framework**: FastAPI
- **Database**: PostgreSQL 16
- **ORM**: SQLAlchemy 2.0 (Async) + asyncpg
- **Migrations**: Alembic
- **Auth**: JWT (jose) + Passlib (bcrypt)
- **Containerization**: Docker & Docker Compose

## Структура проекта
Проект организован по принципу **Feature-based architecture**:
- `app/core/` — общие настройки, база данных, безопасность и зависимости.
- `app/features/users/` — сущности пользователей, репозитории и схемы.
- `app/features/auth/` — логика аутентификации и выдачи токенов.
- `migrations/` — файлы миграций Alembic.
- `scripts/` — вспомогательные скрипты.
