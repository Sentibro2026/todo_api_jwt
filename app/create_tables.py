from app.db import Base, engine
from app import models  # важно: импорт моделей регистрирует их в Base

Base.metadata.create_all(bind=engine)
print("Таблицы созданы")