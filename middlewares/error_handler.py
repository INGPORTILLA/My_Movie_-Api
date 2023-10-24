#Algoritmo para detectar errores en FastAPI
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Union
  

#creamos una clase que herede BaseHTTPMiddleware

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI ) -> None:
        super().__init__(app)
#creamos un metodo que se ejecute y mire si hay errores
    async def dispatch(self, request: Request, call_next) -> Union[Response, JSONResponse]:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})
        