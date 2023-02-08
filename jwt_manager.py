

from jwt import encode, decode


def create_token(data: dict) -> str:
    # 1) payload contenido a pasar al token
    # 2) Clave para generara el token
    # 3) Algoritmo para generar el token
    token: str = encode(payload=data, key="mi_clave", algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key="mi_clave", algorithm=["HS256"])
    return data
