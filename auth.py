from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from database import get_db
import secrets

router = APIRouter()

class AplicacaoInput(BaseModel):
    nome: str

class LoginInput(BaseModel):
    nome: str
    token: str

@router.post("/login")
def login(dados: LoginInput, Authorize: AuthJWT = Depends()):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aplicacoes WHERE nome = ? AND token = ?", (dados.nome, dados.token))
    app_data = cursor.fetchone()
    conn.close()

    if not app_data:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    access_token = Authorize.create_access_token(subject=dados.nome)
    refresh_token = Authorize.create_refresh_token(subject=dados.nome)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

@router.post("/registrar-aplicacao")
def registrar_aplicacao(dados: AplicacaoInput):
    nome = dados.nome
    token = secrets.token_hex(32)

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM aplicacoes WHERE nome = ?", (nome,))
    if cursor.fetchone():
        raise HTTPException(status_code=400, detail="Aplicação já registrada.")

    cursor.execute("INSERT INTO aplicacoes (nome, token) VALUES (?, ?)", (nome, token))
    conn.commit()
    conn.close()

    return {"nome": nome, "token": token}

@router.post("/refresh")
def refresh_token(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_refresh_token_required()
        current_user = Authorize.get_jwt_subject()
        new_access_token = Authorize.create_access_token(subject=current_user)
        return {"access_token": new_access_token}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Refresh token inválido ou expirado")
