from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Service Running"}

@app.get("/predict")
def predict():
    return {"result": "AI model prediction"}
