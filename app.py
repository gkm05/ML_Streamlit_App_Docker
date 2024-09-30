from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
# Create a FastAPI application
app = FastAPI()

# Define the input data structure
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define the prediction endpoint
@app.post("/predict")
def predict(data: IrisData):
    # Load the saved model
    with open("iris_model.pkl", "rb") as f:
        model = pickle.load(f)
    data = data.model_dump()

    sl = data['sepal_length']
    sw = data['sepal_width']
    pl = data['petal_length']
    pw = data['petal_width']
    # Make a prediction
    prediction = model.predict([ [sl,sw,pl,pw]])

    return {"species": prediction[0]}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)