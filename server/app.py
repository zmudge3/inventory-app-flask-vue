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

    def __repr__(self):
        return f"<Container id={self.id}>"

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

    def __repr__(self):
        return f"<Item id={self.id}>"


@app.route('/containers', methods=['GET'])
def all_containers():
    containers = Container.query.order_by(Container.date_created).all()
    return jsonify({'containers': [container.serialize for container in containers]})

@app.route('/containers/new', methods=['POST'])
def new_container():
    post_data = request.get_json()
    new_container = Container(name=post_data.get('name'))
    db.session.add(new_container)
    db.session.commit()

    response_object = {'message': 'Container added'}
    return jsonify(response_object)

@app.route('/containers/<container_id>', methods=['GET'])
def view_container(container_id):
    container = Container.query.get_or_404(container_id)
    return jsonify(container.serialize)

@app.route('/containers/<container_id>/new_item', methods=['POST'])
def new_item(container_id):
    post_data = request.get_json()
    container = Container.query.get_or_404(container_id)
    new_item = Item(name=post_data.get('name'), container=container)
    db.session.add(new_item)
    db.session.commit()
 
    response_object = {'message': 'Item added'}
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
