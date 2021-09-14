from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true
from fastapi.encoders import jsonable_encoder
from .models import Product


from . import models, schemas

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def put_product(db: Session, product_id: int,  product: schemas.ProductCreate):

    """

    db
    product_id
    """
    product_upd=product.dict()
    db_product =db.query(models.Product).filter(models.Product.id == product_id).first()
    db.query(models.Product).filter(models.Product.id == product_id).update(product_upd,'fetch')
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



