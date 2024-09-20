from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Tic-Tac-Toe field as a 3x3 grid initialized with empty spaces
field = [[' ' for _ in range(3)] for _ in range(3)]

# Model for receiving player move requests
class Move(BaseModel):
    row: int
    col: int

# Function to print the current field as a string
def print_field():
    rows = []
    for row in field:
        rows.append(' | '.join(row))
    return '\n---------\n'.join(rows)

# Endpoint to place an 'X' on the board
@app.post("/place_x/")
async def place_x(move: Move):
    row, col = move.row, move.col

    # Check if the move is valid (within bounds)
    if row < 0 or row > 2 or col < 0 or col > 2:
        raise HTTPException(status_code=400, detail="Invalid position, must be between 0 and 2.")

    # Check if the spot is already taken
    if field[row][col] != ' ':
        raise HTTPException(status_code=400, detail="Position already taken.")

    # Place 'X' on the field
    field[row][col] = 'X'
    return {"message": "Move placed!", "field": print_field()}

# Endpoint to get the current state of the field
@app.get("/field/")
async def get_field():
    return {"field": print_field()}
