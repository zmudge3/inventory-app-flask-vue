from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

# instantiate the app
db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

class Container(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    items = db.relationship('Item', backref='container')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'items': [item.serialize for item in self.items],
        }

    # def __repr__(self):
    #     return f'<Container "{self.id}, {self.name}">'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    container_id = db.Column(db.Integer, db.ForeignKey('container.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    # def __repr__(self):
    #     return f'<Item "{self.id}, {self.name}">'


CONTAINERS = {
    'd9cb84d4c2384b65aaa31f8be7aedfa8': {
        'name': 'Plastic Tote 1',
        'items': ['19de7cac23f6483ca82552b3d9c98205', '3d4c0fab1eb841e8bbef6e67f148fd77'],
    },
    '04bab8f1da1d40a88fa02c5620478608': {
        'name': 'Plastic Tote 2',
        'items': ['5f2ecff9037d4fc88b8539d9f5b1e9e1', 'e5a337699083470d9c007529531f9fd5'],
    },
    '4107de7cf55646e48b823b36b0841eff': {
        'name': 'Drawer 1',
        'items': ['60290617555f4a548d60c55e0eaae4f3', 'b02c9bc1e124408284708df3d9ba396b'],
    },
}

ITEMS = {
    '19de7cac23f6483ca82552b3d9c98205': {
        'name': 'Item1-1',
        'container_id': 'd9cb84d4c2384b65aaa31f8be7aedfa8',
    },
    '3d4c0fab1eb841e8bbef6e67f148fd77': {
        'name': 'Item1-2',
        'container_id': 'd9cb84d4c2384b65aaa31f8be7aedfa8',
    },
    '5f2ecff9037d4fc88b8539d9f5b1e9e1': {
        'name': 'Item2-1',
        'container_id': '04bab8f1da1d40a88fa02c5620478608',
    },
    'e5a337699083470d9c007529531f9fd5': {
        'name': 'Item2-2',
        'container_id': '04bab8f1da1d40a88fa02c5620478608',
    },
    '60290617555f4a548d60c55e0eaae4f3': {
        'name': 'Item3-1',
        'container_id': '4107de7cf55646e48b823b36b0841eff',
    },
    'b02c9bc1e124408284708df3d9ba396b': {
        'name': 'Item3-2',
        'container_id': '4107de7cf55646e48b823b36b0841eff',
    },
}

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/containers', methods=['GET'])
def all_containers():
    containers = Container.query.order_by(Container.date_created).all()
    return jsonify({'containers': [container.serialize for container in containers]})

@app.route('/new', methods=['POST'])
def new_container():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    new_container_id = uuid.uuid4().hex
    CONTAINERS[new_container_id] = {
        'name': post_data.get('name'),
        'items': []
    }
    response_object['message'] = 'Container added'
    return jsonify(response_object)

@app.route('/<container_id>', methods=['GET'])
def view_container(container_id):
    container = CONTAINERS[container_id]
    items = [ITEMS[item_id] for item_id in container['items']]
    return jsonify({
        'status': 'success',
        'name': container['name'],
        'items': items,
    })

@app.route('/<container_id>/new_item', methods=['POST'])
def new_item(container_id):
    response_object = {'status': 'success'}
    post_data = request.get_json()
    new_item_id = uuid.uuid4().hex
    ITEMS[new_item_id] = {
        'name': post_data.get('name'),
        'container_id': container_id,
    }
    CONTAINERS[container_id]['items'].append(new_item_id)
    response_object['message'] = 'Item added'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
