


from typing import List
from fastapi import FastAPI
from fastapi.responses import FileResponse

import sys

from model.pokedex_model import Pokemon
#from resources.resource_pokedex import PokeDexResource
from data.pokedex_repository import PokeDexRepository


app = FastAPI()

pokedex = PokeDexRepository()


@app.get("/pokemon/page/{page}", response_model=List[Pokemon])
async def get_pokemon_by_page(page: int):
    """
        curl http://127.0.0.1/pokemon/page/{page}
    """
    return pokedex.getPokemonByPage(page=page)

@app.get("/pokemon/{id}", response_model=Pokemon)
async def get_pokemon_by_id(id: str):
    """
        curl http://127.0.0.1/pokemon/{id}
    """
    return pokedex.getPokemonById(nameId=id)


@app.get("/images/{name}.png", response_class=FileResponse)
async def get_image(name: str):
    return f'images/{name}.png'