
from typing import List
from model.pokedex_model import Pokemon
from data.pokedex_repository import PokeDexRepository

class PokeDexResource():
    def __init__(self, repository: PokeDexRepository):
        self.repository = repository

    def getPokemonByPage(self, page: int) -> List[Pokemon]:
        if page < 1 or page > 15:
            page = 1
        return self.repository.getPokemonByPage(page = page)