from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Produto:
    id: Optional[int] = None 
    nome: Optional[str] = None 
    descricao: Optional[str] = None 
    estoque: Optional[str] = None 
    preco: Optional[str] = None 
    categoria: Optional[str] = None 