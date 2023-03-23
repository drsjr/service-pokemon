import json
from typing import List
from model.pokedex_model import Pokemon, Names

class PokeDexRepository():
    def __init__(self):
        self.dataset = dict()
        file = open('dataset/pokedex.json', 'r').read()
        jsonList = json.loads(file)
        for item in jsonList:
            self.dataset[item["nameId"]] = Pokemon(
                id = item["id"],
                nameId = item["nameId"],
                name = item["name"]["english"],
                type = item["type"]
            )
        self.keys = list(self.dataset.keys())


    def getPokemonByPage(self, page: int) -> List[Pokemon]:
        page =  page - 1
        start = (page * 10)
        end = start + 10
        keys = self.keys[start:end]
        return [self.dataset[i] for i in keys]

    def getPokemonById(self, nameId: str) -> Pokemon:
        if nameId in self.keys:
            return self.dataset[nameId]
        else:
            return self.dataset["001"]
