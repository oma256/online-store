from flask import Blueprint, jsonify, request

from models import Item, Product, db
from schemas import ProductSchema


products_bp = Blueprint('products', __name__)


@products_bp.route('/get_list', 
                   methods=['GET', 'POST'], 
                   endpoint='get_products')
def get_list():
    item_id = request.args.get('item_id')
    store_id = request.args.get('store_id')
    query = db.session.query(Product)

    if item_id:
        query = query.filter_by(item_id=item_id)

    if store_id:
        query = query.filter_by(store_id=store_id)

    product_schema = ProductSchema(many=True)
    product_list = product_schema.dump(query)

    return jsonify({'code': 0, 'list': product_list})
