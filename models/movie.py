#importamos 
from config.database import Base
from sqlalchemy import Column, Integer, String, Float

#creamos una clase movie que sera la entidad de la base de datos
class Movie(Base):

#indicamos el nombre de la tabla
    __tablename__ = "movies"

#ahora empezamos con los campos de la tabla
    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    


