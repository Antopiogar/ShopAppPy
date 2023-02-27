from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    id: Optional[int]
    nome: str 
    qta: int
    
    def setId(self, id):
        self. id  = id
    
    def setNome(self, nome):
        self. nome  = nome
    
    def setQta(self, qta):
        self. qta  = qta

    def __str__(self) -> str:
        return f""" id:{self.id },
                    nome:"{self.nome }", 
                    qta:{self.qta }
                """
    
