from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    """Handles GET for routeing login form"""
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    """Handles POST for login"""
    if username == "admin" and password == "admin123": 
        return {"message": "Login successful!"}
    raise HTTPException(status_code=401, detail="Invalid username or password")
