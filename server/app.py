from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

    def __repr__(self):
        return f"<Container id={self.id}, name={self.name}>"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    container_id = db.Column(db.Integer, db.ForeignKey('container.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
        }

    def __repr__(self):
        return f"<Item id={self.id}, name={self.name}>"


@app.route('/api/containers', methods=['GET'])
def all_containers():
    containers = Container.query.order_by(Container.date_created).all()
    return jsonify({'containers': [container.serialize for container in containers]})

@app.route('/api/containers/new', methods=['POST'])
def new_container():
    post_data = request.get_json()
    new_container = Container(name=post_data.get('name'))
    db.session.add(new_container)
    db.session.commit()

    response_object = {'message': 'Container added'}
    return jsonify(response_object)

@app.route('/api/containers/<container_id>', methods=['GET', 'DELETE', 'PUT'])
def view_container(container_id):
    if request.method == 'GET':
        container = Container.query.get_or_404(container_id)
        return jsonify(container.serialize)
    elif request.method == 'DELETE':
        container_to_delete = Container.query.get_or_404(container_id)
        db.session.delete(container_to_delete)
        db.session.commit()

        response_object = {'message': 'Container deleted'}
        return jsonify(response_object)
    else:
        container_to_edit = Container.query.get(container_id)
        put_data = request.get_json()
        container_to_edit.name = put_data.get('name')
        db.session.commit()

        response_object = {'message': 'Container updated'}
        return jsonify(response_object)


@app.route('/api/containers/<container_id>/new_item', methods=['POST'])
def new_item(container_id):
    post_data = request.get_json()
    container = Container.query.get_or_404(container_id)
    new_item = Item(
        name=post_data.get('name'),
        quantity=post_data.get('quantity'),
        container=container)
    db.session.add(new_item)
    db.session.commit()
 
    response_object = {'message': 'Item added'}
    return jsonify(response_object)

@app.route('/api/items/<item_id>', methods=['DELETE', 'PUT'])
def delete_item(item_id):
    if request.method == 'DELETE':
        item_to_delete = Item.query.get_or_404(item_id)
        db.session.delete(item_to_delete)
        db.session.commit()

        response_object = {'message': 'Item deleted'}
        return jsonify(response_object)
    else:
        item_to_edit = Item.query.get(item_id)
        put_data = request.get_json()
        item_to_edit.name = put_data.get('name')
        item_to_edit.quantity = put_data.get('quantity')
        db.session.commit()

        response_object = {'message': 'Item updated'}
        return jsonify(response_object)


if __name__ == '__main__':
    app.run()
