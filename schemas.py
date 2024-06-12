from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Category, Item, Product, Store


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True


class ItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True


class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True


class StoreSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Store
        load_instance = True
