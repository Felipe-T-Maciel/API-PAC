from datetime import datetime, timedelta
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "felipe_e_perfeito"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
      payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
      return payload
    except JWTError:
      return None
