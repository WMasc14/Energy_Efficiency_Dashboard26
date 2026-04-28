from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from Simulator import run_simulation

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

# Serve the production React build if it exists
try:
    app.mount(
        "/",
        StaticFiles(directory="dist", html=True),
        name="static",
    )
except RuntimeError:
    # Directory 'dist' does not exist, skip static files
    pass
