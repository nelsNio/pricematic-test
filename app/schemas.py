from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    nombre: str 
    precio:int
    fecha_insercion:date



class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
