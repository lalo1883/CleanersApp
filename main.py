from email.policy import default
from unicodedata import category
from urllib.request import Request

import fastapi
from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token
from fastapi.security import HTTPBearer

from starlette.responses import JSONResponse

app = FastAPI()
app.title = "Documentación de peliculas."  # cambiar el titulo de la documentación
app.version = "1.0.0"  # cambiar la version de la documentation


# Atributos de la clase movie
class Cleaner(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="John Doe", min_length=5, max_length=15)
    age: int = Field(default=30, ge=18, le=70)
    hourly_rate: float = Field(default=20.0, ge=10.0)
    city: str = Field(default="New York", min_length=5, max_length=15)



cleaners = [
    {
        'id': 1,
        'name': 'Jane Doe',
        'age': 35,
        'hourly_rate': 25.0,
        'city': "Los Angeles",
    },
    {
        'id': 2,
        'name': 'John Smith',
        'age': 40,
        'hourly_rate': 30.0,
        'city': "New York",
    },
    {
        'id': 3,
        'name': 'Jane Smith',
        'age': 25,
        'hourly_rate': 20.0,
        'city': "San Francisco",
    }
]



@app.get("/", tags=["home"])  # Agrupar rutas  esta es home
async def root():
    return HTMLResponse(" <h1>Hello world</h1>")


@app.get("/cleaners", tags=["Cleaners"], response_model=List[Cleaner])
def get_cleaner() -> List[Cleaner]:
    return JSONResponse(content=cleaners)


# parametro id
@app.get("/cleaners/{id}", tags=["Cleaners"], response_model=Cleaner)
def get_cleaner_(id: int = Path(le=2000, ge=0)) -> Cleaner:  # Parametros a pedir
    for item in cleaners:
        if item['id'] == id:
            return JSONResponse(content=item)
    return []


# parametro query
@app.get("/cleaner/", tags=["Cleaners"], response_model=List[Cleaner])
def get_cleaner_by_city(city: str = Query(min_length=5, max_length=15)) -> List[Cleaner]:
    data = list(filter(lambda x: x["city"] == city, cleaners))
    return JSONResponse(content=data)


@app.post("/cleaner/", tags=["Cleaners"], response_model=dict)
def create_movie(movie: Cleaner) -> dict:
    cleaners.append(movie)
    return JSONResponse(content={'message': 'se ha registrado el personal'})


@app.put("/cleaner/{id}", tags=["Cleaners"], response_model=dict)
def edit_cleaner(id: int, cleaner: Cleaner) -> dict:
    for item in cleaners:
        if item['id'] == Cleaner.id:
            item['name'] = Cleaner.name
            item['hourly_rate'] = Cleaner.hourly_rate
            item['city'] = Cleaner.city
            return JSONResponse(content={'message': 'se han actualizado los datos'})


@app.delete("/cleaner/{id}", tags=["Cleaner"], response_model=dict)
def delete_cleaner(id: int) -> dict:
    for item in cleaners:
        if item['id'] == id:
            Cleaner.remove(item)
            return JSONResponse(content={'message': 'se ha eliminado el persona'})
