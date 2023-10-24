#creamos un router para autenticarnos
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from pydantic import BaseModel
from schema.user import User

#creamos una variable
user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        #el método .dict() esta en des uso. Se debe usar "movie.model_dump()"
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
            