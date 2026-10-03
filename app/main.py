from fastapi import FastAPI

from app.routes import auth, tasks

app = FastAPI(
    title="TODO API с JWT",
    version="1.0.0",
)

app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "TODO API работает"}