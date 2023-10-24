# algoritmo que nos permite trabajar con routers
from fastapi import APIRouter
# importamnos el modulo fastapi,body,path
from fastapi import Depends,Path, Query, Request, HTTPException

#importamos el modulo HTML,json
from fastapi.responses import HTMLResponse, JSONResponse

#importamos Basemodel para crear un esquema, y field para validar datos
from pydantic import BaseModel, Field

#importamos optional para dar valores opcionales, List para crear una lista de peliculas
from typing import Optional, List

# desde jwt_manager importamos create_token
from utils.jwt_manager import create_token, validate_token

# importamos security ...
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from config.database import Session, engine, Base
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from services.movie import MovieService
from schema.movie import Movie
from middlewares.jwt_bearer import JWTBearer
#creamos una variable
movie_router = APIRouter()

# Usamos get para consultar en movies y agregamos una tags, y dependencies que pone el candado de inicio de sesion con token
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
    
#definimos la funcion, usamos Jsonresponse,List
def get_movies() -> List[Movie]:
#creamos una sesion para consultar los datos usando query
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

# usamos Session y filter, path para validar parametros
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
       return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
    
#agregamos una nueva ruta para para usar query,list
@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])

#definimos la funcion y agregamos parametros year, usamos Query, list,session
def get_movies_by_year(year: str = Query(min_length=4, max_length=15)) -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.year == year).all()
    if not result:
       return JSONResponse(status_code=404, content={'message': "Año no valido"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
 
# usamos el metodo JSON
    data = [item for item in movies if item['year'] == year ]
    return JSONResponse(content=data)

# usamos el metodo POST con esquema, JSON

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})

# usamos PUT para modificar una movie, JSON
@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    db.commit()
    return JSONResponse(status_code=200,content={"message": "se ha modificado la pelicula"})
        
# usamos DELETE para eliminar una movie, JSONresponse, Session 
@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()      
    return JSONResponse(status_code=200,content={"message": "se ha eliminado la pelicula"})
