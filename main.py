from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from auth import router as auth_router
from spell_check import corrigir_frase
from config import Settings
from fastapi_jwt_auth import AuthJWT
from database import init_db

app = FastAPI()

templates = Jinja2Templates(directory="templates")

init_db()

app.include_router(auth_router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/corrigir-frase")
def corrigir_texto(data: dict, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    frase = data.get("frase", "")
    return {"frase corrigida": corrigir_frase(frase)}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

