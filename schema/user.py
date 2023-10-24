#este codigo crea datos para usuario en la movie

from pydantic import BaseModel

#creamos una clas tipo user
class User(BaseModel):
    email: str
    password: str