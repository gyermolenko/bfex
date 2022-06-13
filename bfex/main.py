from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from bfex import find_checks

app = FastAPI()

templates = Jinja2Templates(directory="bfex/templates")


@app.get("/", response_class=HTMLResponse)
def find_a_check_get_exercise(request: Request):
    board = find_checks.set_board_for_find_a_check()
    return templates.TemplateResponse("find_check.html", {"request": request, "board": str(board).split("\n")})


@app.post("/find_a_check/")
def find_a_check_make_a_move(move: str = Form()):
    return {"move played": move}
