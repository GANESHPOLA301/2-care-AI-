from fastapi import FastAPI
from backend.routes.appointment_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"status": "running"}
