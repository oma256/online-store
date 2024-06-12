import json
from models import Category
from utils import create_app


app = create_app()


@app.route('/upload_data_to_db')
def upload_data_to_db():
    with open('./data_to_db/categories.json', 'r') as f:
        categories = json.load(f)

        for category in categories:
            c = Category(name=category['name'])
            
    return {'status': 'OK'}
