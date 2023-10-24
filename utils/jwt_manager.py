from jwt import encode, decode

#definimos la funcion y le enviamos el data que es tipo dict
def create_token(data: dict):

#creamos la variable token y guardamos el payload y la key, y usamos el algoritmo 256
    token: str = encode(payload=data, key="my_secrete_key", algorithm="HS256")
    return token

#creamos la funcion para validar el token
#encode -> crea el token
#decode -> valida el token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secrete_key", algorithms=['HS256'])
    return data

