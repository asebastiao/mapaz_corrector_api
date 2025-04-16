# Corrector API - CORRECTOR ORTOGRÁFICO PARA O MAPAZZZ - KandenguesCode

Uma API de correção ortográfica desenvolvida com **FastAPI**, com suporte a **autenticação JWT** e **proteção via token de API personalizado** por aplicação. Esta API pode ser usada por sistemas externos (como aplicações Laravel) para correção de palavras ou frases em português.

---

## 🚀 Funcionalidades

- Registro e login de usuários com autenticação JWT
- Emissão e verificação de tokens JWT (`access` e `refresh`)
- Geração de **tokens de API personalizados por aplicação**
- Endpoints protegidos para correção ortográfica de palavras e frases
- Correção ortográfica baseada na biblioteca `pyspellchecker`

---

## 🧰 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PySpellChecker](https://github.com/barrust/pyspellchecker)
- [fastapi-jwt-auth](https://github.com/IndominusByte/fastapi-jwt-auth)
- [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)

---

## 🔧 Instalação

Crie um ambiente virtual e ative:

python3 -m venv venv #(o directório Corrector API já possui um ambiente virtual, então podes simplesmente tentar activar)
source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Inicie a aplicação:
uvicorn main:app --reload

Token de Autorizacao possuem uma hora de duração antes de expirar, se expirar pode usar o token de refresh(que tem duração de um dia) para obter um novo token de autorização.