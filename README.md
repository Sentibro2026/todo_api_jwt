# TODO API with JWT

REST API for managing tasks with JWT authentication.
Users can register, log in, and manage only their own tasks.

---

## Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT (python-jose)
- passlib + bcrypt
- Uvicorn

---

## Features

- User registration
- JWT authentication
- CRUD operations for tasks
- Filter tasks by status
- Users can only access their own tasks
- Auto-generated Swagger docs

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/Sentibro2026/todo_api_jwt.git
cd todo_api_jwt
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate it

Windows:
```bash
.venv\Scripts\activate
```

Linux / macOS:
```bash
source .venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create `.env` based on `.env.example`

```bash
cp .env.example .env
```

6. Create the database

```sql
CREATE DATABASE todo_db;
```

7. Create tables

```bash
python -m app.create_tables
```

8. Run the server

```bash
uvicorn app.main:app --reload
```

---

## Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Examples

Register

```http
POST /auth/register
Content-Type: application/json

{ 
  "email": "test@mail.com",
  "password": "123456"
}
```

Login

```
POST /auth/login
username=test@mail.com&password=123456
```

Create Task

```
POST /tasks
Authorization: Bearer <token>
{
  "title": "Buy milk",
  "description": "Two liters"
}
```

---

## Project Structure

```
app/
├── main.py
├── config.py
├── db.py
├── models.py
├── schemas.py
├── auth.py
├── deps.py
├── create_tables.py
└── routes/
    ├── auth.py
    └── tasks.py
```

---

## Author

Stepan Ivashchenko