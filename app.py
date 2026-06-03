from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# FastAPI Object
app = FastAPI()

# Load Trained Model
model = joblib.load("salary_model.joblib")

# Input Schema
class Employee(BaseModel):
    experience: float

# Home Route
@app.get("/")
def home():
    return {
        "message": "Salary Prediction API Running abc"
    }

# Prediction Route
@app.post("/predict")
def predict_salary(data: Employee):

    exp = np.array([[data.experience]])

    prediction = model.predict(exp)

    return {
        "experience": data.experience,
        "predicted_salary": float(prediction[0])
<<<<<<< HEAD
    }
=======
    }
>>>>>>> 32fb8fde3f67521194b13db52025939154d6cfc1
