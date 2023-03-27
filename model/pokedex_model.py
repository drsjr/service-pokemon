
from typing import List
from pydantic import BaseModel

"""
{
    "id": 1,
    "nameId": "001",
    "name": {
      "english": "Bulbasaur",
      "japanese": "フシギダネ",
      "chinese": "妙蛙种子",
      "french": "Bulbizarre"
    },
    "type": [
      "Grass",
      "Poison"
    ],
    "base": {
      "HP": 45,
      "Attack": 49,
      "Defense": 49,
      "Sp. Attack": 65,
      "Sp. Defense": 65,
      "Speed": 45
    }
  }
"""

class Names(BaseModel):
    english: str
#    japanese: str
#    chinese: str
#    french: str

class Pokemon(BaseModel):
    id: str
    nameId: str
    name: str
    type: List[str]
    url: str
