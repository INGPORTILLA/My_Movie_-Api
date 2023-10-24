
#Este archivo lo usamos para configurar la conexion con la base de datos en FastAPI
#import modulo Os, create_engine

import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import File

#creamos las variables
sqlite_file_name= "../database.sqlite"

#leemos el directorio de os
base_dir = os.path.dirname(os.path.realpath(__file__))


 #creamos la variable de la base de datos, usamos join para unir las dos variables
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"



#creamos una variable para el motor de la base de datos
engine = create_engine(database_url, echo=True)


#creamos una variable para conectarnos a la base de datos

Session = sessionmaker(bind=engine)

#creamos unavariable para el manejo de datos
Base = declarative_base()
