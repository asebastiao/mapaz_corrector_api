from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv()

class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("JWT_SECRET_KEY")
    authjwt_access_token_expires: timedelta = timedelta(
        minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 60))
    )
    authjwt_refresh_token_expires: timedelta = timedelta(
        minutes=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", 1440))
    )

@AuthJWT.load_config
def get_config():
    return Settings()
