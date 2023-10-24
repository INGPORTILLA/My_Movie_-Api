from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import create_token, validate_token

#Creamos una clase JWTBearer y la funcion para solictar el token al usuario
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="credenciales incorrectas")