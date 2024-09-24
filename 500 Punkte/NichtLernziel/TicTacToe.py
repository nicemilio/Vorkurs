from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    row1: str | None = None
    row2: str | None = None
    row3: str | None = None


field = {
    1: ["[]", "[]", "[]"],
    2: ["[]", "[]", "[]"],
    3: ["[]", "[]", "[]"],
}

def fieldEmpty (x: int, y:int) -> bool:
    if (field [x][y] in {"[X]", "[O]"}):
        return False
    return True

def makeMove() -> None:
    def testMove(x: int, y: int, symbol: str) -> bool:
        field[x][y] = symbol
        if checkWin():
            field[x][y] = "[]"  # Reset after test
            return True
        field[x][y] = "[]"  # Reset after test
        return 

    for x in range(1, 4):
        for y in range(3):
            if fieldEmpty(x, y):
                if testMove(x, y, "[O]"):
                    field[x][y] = "[O]" 
                    return

    for x in range(1, 4):
        for y in range(3):
            if fieldEmpty(x, y):
                if testMove(x, y, "[X]"):  # Can player win by moving here?
                    field[x][y] = "[O]"  # Block opponent's winning move
                    return

    for x in range(1, 4):
        for y in range(3):
            if fieldEmpty(x, y):
                field[x][y] = "[O]"  # Make the move
                return

    markWin ("[D]")

            
def checkWin() -> bool:
    for row in range(1, 4):
        if field[row][0] == field[row][1] == field[row][2] and field[row][0] in {"[X]"}:
            return "[X]"
        elif field[row][0] == field[row][1] == field[row][2] and field[row][0] in {"[0]"}:
            return "[O]"

    for col in range(3):
        if field[1][col] == field[2][col] == field[3][col] and field[1][col] in {"[X]"}:
            return "[X]"
        elif field[1][col] == field[2][col] == field[3][col] and field[1][col] in {"[O]"}:
            return "[O]"

    if field[1][0] == field[2][1] == field[3][2] and field[1][0] in {"[X]"}:
        return "[X]"
    if field[1][0] == field[2][1] == field[3][2] and field[1][0] in {"[O]"}:
        return "[O]"
    if field[1][2] == field[2][1] == field[3][0] and field[1][2] in {"[X]"}:
        return "[X]"
    if field[1][2] == field[2][1] == field[3][0] and field[1][2] in {"[O]"}:
        return "[O]"

    return ""

def markWin (symbol: str) -> None:
    for x in range (1, 4):
        for y in range (0, 3):
            field [x] [y] = symbol

@app.get("/field", response_model=Item)
async def read_item():
    return {
        "row1": ", ".join(field[1]),
        "row2": ", ".join(field[2]),
        "row3": ", ".join(field[3]),
    }


@app.put("/place/{x}/{y}", response_model=Item)
async def place_X(x: int, y: int):
    y -= 1
    if fieldEmpty (x, y):
        field [x] [y] = "[X]"
        if not checkWin ():
            makeMove ()
        winChar = checkWin ()
        if winChar:
            markWin (winChar)
    return {
        "row1": ", ".join(field[1]),
        "row2": ", ".join(field[2]),
        "row3": ", ".join(field[3]),
    }