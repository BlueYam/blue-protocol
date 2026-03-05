from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt

from app.core.config import CONFIG

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def verify_pass(plain_pass: str, hashed_pass: str) -> bool:
    return pwd_context.verify(plain_pass, hashed_pass)

def get_pass_hash(password: str) -> str:
    return pwd_context.hash(password)