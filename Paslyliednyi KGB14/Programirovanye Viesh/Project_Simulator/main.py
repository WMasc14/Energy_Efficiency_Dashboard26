from fastapi import FastAPI
from pydantic import BaseModel
from Simulator import run_simulation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Params(BaseModel):
    CA0: float
    F: float
    V: float
    k: float
    time: float

@app.post("/simulate")
def simulate(params: Params):
    return run_simulation(params.dict())