from fastapi import FastAPI
from pydantic import BaseModel
from calculator import SmartCalculator

app = FastAPI()

calculator = SmartCalculator()

class OperationRequest(BaseModel):
    a: float
    b: float

class SingleInputRequest(BaseModel):
    x: float

class ExpressionRequest(BaseModel):
    expression: str

@app.post("/add")
def add(req: OperationRequest):
    return {"result": calculator.add(req.a, req.b)}

@app.post("/subtract")
def subtract(req: OperationRequest):
    return {"result": calculator.subtract(req.a, req.b)}

@app.post("/multiply")
def multiply(req: OperationRequest):
    return {"result": calculator.multiply(req.a, req.b)}

@app.post("/divide")
def divide(req: OperationRequest):
    return {"result": calculator.divide(req.a, req.b)}

@app.post("/power")
def power(req: OperationRequest):
    return {"result": calculator.power(req.a, req.b)}

@app.post("/modulus")
def modulus(req: OperationRequest):
    return {"result": calculator.modulus(req.a, req.b)}

@app.post("/sqrt")
def sqrt(req: SingleInputRequest):
    return {"result": calculator.sqrt(req.x)}

@app.post("/log")
def log(req: SingleInputRequest):
    return {"result": calculator.log(req.x)}

@app.get("/history")
def history():
    return {"history": calculator.history}

@app.post("/evaluate")
def evaluate_expression(req: ExpressionRequest):
    return {"result": calculator.evaluate_expression(req.expression)}
