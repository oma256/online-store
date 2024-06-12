
from routes.categories import categories_bp
from routes.items import items_bp
from routes.products import products_bp
from routes.stores import stores_bp


def init(app):
    app.register_blueprint(categories_bp, url_prefix='/api/v1/categories')
    app.register_blueprint(items_bp, url_prefix='/api/v1/items')
    app.register_blueprint(products_bp, url_prefix='/api/v1/products')
    app.register_blueprint(stores_bp, url_prefix='/api/v1/stores')
