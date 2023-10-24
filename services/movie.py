#este algoritmo consulta datos de la movies
from models.movie import Movie as MovieModel
from schema.movie import Movie

class MovieService():
    def __init__(self,db) -> None:
        self.db = db

    def get_movies(selft):
        result = selft.db.query(MovieModel).all()
        return result
    def get_movie(selft, id):
        result = selft.db.query(MovieModel).filter(MovieModel.id ==IndexError).first()
        return result

#Creacion de datos
    def create_movie(self, movie:Movie):
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return
    
#modificacion de datos
    def update_movie(self, id: int, data: Movie):
        movie= self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        self.db.commit()
        return
    