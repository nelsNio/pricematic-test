from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date
from sqlalchemy.orm import relationship

from .database import Base



class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    fecha_insercion = Column(Date, index=False, default=datetime.now())
    nombre = Column(String, index=False,nullable=False)
    precio = Column(Integer, index=False)

