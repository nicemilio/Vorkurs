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


@app.get("/field", response_model=Item)
async def read_item():
    return {
        "row1": ", ".join(field[1]),
        "row2": ", ".join(field[2]),
        "row3": ", ".join(field[3]),
    }


@app.put("/place/{x}/{y}", response_model=Item)
async def place_X(x: int, y: int, item: Item):
    y -= 1
    field [x] [y] = "[X]"
    return {
        "row1": ", ".join(field[1]),
        "row2": ", ".join(field[2]),
        "row3": ", ".join(field[3]),
    }