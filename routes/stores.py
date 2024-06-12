from flask import Blueprint, jsonify

from models import Store, db
from schemas import StoreSchema


stores_bp = Blueprint('stores', __name__)


@stores_bp.route('/get_list', methods=['GET', 'POST'], endpoint='get_stores')
def get_list():
    stores = db.session.query(Store).all()

    store_schema = StoreSchema(many=True)
    categories_list = store_schema.dump(stores)

    return jsonify({'code': 0, 'list': categories_list})


