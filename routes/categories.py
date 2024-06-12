from flask import Blueprint, jsonify

from models import Category, db
from schemas import CategorySchema


categories_bp = Blueprint('categories', __name__)


@categories_bp.route('/get_list', 
                     methods=['GET', 'POST'], 
                     endpoint='get_categories')
def get_list():
    categories = db.session.query(Category).all()

    category_schema = CategorySchema(many=True)
    categories_list = category_schema.dump(categories)
    
    return jsonify({'code': 0, 'list': categories_list})
