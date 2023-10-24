# importamnos el modulo fastapi,body,path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from config.database import engine, Base
from routers.movie import movie_router
from middlewares.error_handler import ErrorHandler
from routers_2.user import user_router

#creamos una instancia de fastapi
app= FastAPI()

#Cambiamos el titulo a la app en swager
app.title = "ING PORTILLA MOVIES APLICATION"

#modificamos la version
app.version = "0.0.1"


#llamamos al archivo error,router
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)
#llamamos Base
Base.metadata.create_all(bind=engine)
  
#creamos la variable movies con la lista de la pelicula
movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un planeta llamado INGPORTILLA",
        "year": "2023",
        "category": "Accion ING"
    },
    {
       
        "id": 2,
        "title": "Avatar2",
        "overview": "En un planeta llamado INGPORTILLA",
        "year": "2023",
        "category": "Accion ING2"
    }
]
# ruta de inicio, cambiamos el home
@app.get('/', tags=['home ING'])

#definimos la funcion
def message():
# escribimos el mensaje en HTML
    return HTMLResponse('<h1>HOLA ING PORTILLA</h1>')



        

        




