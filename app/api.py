from fastapi import FastAPI
from pydantic import BaseModel
from app.main import main

class StartInput(BaseModel):
    # ai_name should be a string
    ai_name: str

    # ai_role should be a string
    ai_role: str

    #ai_goals should be an array of strings
    ai_goals: list[str]

api = FastAPI()


@api.post("/start")
def do_start(input: StartInput):
    response = main(input.ai_name, input.ai_role, input.ai_goals)
    return response
