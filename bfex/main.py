from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from bfex import find_checks

app = FastAPI()

templates = Jinja2Templates(directory="bfex/templates")


@app.get("/", response_class=HTMLResponse)
def find_checks_get_exercise(request: Request):
    board = find_checks.set_board_for_find_a_check()
    board_alg = find_checks.convert_board_to_algebraic(board)
    return templates.TemplateResponse(
        "find_checks.html", {"request": request, "board": str(board).split("\n"), "board_alg": board_alg}
    )


class Solution(BaseModel):
    move: str
    board_alg: dict


class Result(BaseModel):
    result: str


@app.post("/find_checks/", response_model=Result)
def find_checks_submit_solution(solution: Solution):
    board = find_checks.convert_algebraic_to_board(solution.board_alg)

    try:
        in_check = find_checks.check_solution(board, solution.move)
    except ValueError:
        return {"result": "invalid move"}

    if in_check:
        return {"result": "check"}

    return {"result": "not a check"}
