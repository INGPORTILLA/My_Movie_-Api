#este algoritmo me registra datos en movie
from pydantic import BaseModel,Field
from typing import Optional

#creamos una class movie
class Movie(BaseModel):
    id: Optional[int] = None
#Usamos la validacion de datos min, max , default= por defecto
    title: str = Field(default= "mi pelicula", min_length=5,max_length=15)
    overview: str = Field(default= "descripcion de la pelicula", min_length=15,max_length=50)
    year: int = Field(default=2022, le=2022)