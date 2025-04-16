from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
from dotenv import load_dotenv
from openai import OpenAI
import os

router = APIRouter()
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

class TextoEntrada(BaseModel):
    frase: str

@router.post("/corrigir-frase")
def corrigir_frase(dados: TextoEntrada, Authorize: AuthJWT = Depends()):
    prompt = f"Corrija a frase a seguir em português, mantendo o significado original (usando Português de Portugal):\n\n{dados}\n\nRetorne apenas a frase corrigida."

    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            extra_headers={
                #"HTTP-Referer": "https://seudominio.com",
                "X-Title": "API Corrector MapaZZZ - v1.0",
            }
        )
        frase_corrigida = resposta.choices[0].message.content.strip()
        return {
            "original": dados,
            "corrigida": frase_corrigida
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a frase: {str(e)}")
