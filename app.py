from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Kayla 👋 Your RBAC API is working!"}

@app.get("/admin")
def admin():
    return {"message": "Welcome Admin 🔐"}