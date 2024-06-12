from flask import Blueprint, jsonify, request

from models import Item, db
from schemas import ItemSchema


items_bp = Blueprint('items', __name__)


@items_bp.route('/get_list', 
                methods=['GET', 'POST'], 
                endpoint='get_categories')
def get_list():
    category_id = request.args.get('category_id')
    if category_id:
        items = db.session.query(Item).filter_by(category_id=category_id)
    else:
        items = db.session.query(Item).all()

    item_schema = ItemSchema(many=True)
    items_list = item_schema.dump(items)
    
    return jsonify({'code': 0, 'list': items_list})
