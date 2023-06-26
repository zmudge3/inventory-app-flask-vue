from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

ITEMS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Item1-1',
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Item1-2',
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Item2-1',
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Item2-2',
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Item3-1',
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Item3-2',
    },
]

CONTAINERS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Plastic Tote 1',
        'items': [ITEMS[0]['id'], ITEMS[1]['id']],
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Plastic Tote 2',
        'items': [ITEMS[2]['id'], ITEMS[3]['id']],
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Drawer 1',
        'items': [ITEMS[4]['id'], ITEMS[5]['id']],
    },
]

ITEMS[0]['container_id'] = CONTAINERS[0]['id']
ITEMS[1]['container_id'] = CONTAINERS[0]['id']
ITEMS[2]['container_id'] = CONTAINERS[1]['id']
ITEMS[3]['container_id'] = CONTAINERS[1]['id']
ITEMS[4]['container_id'] = CONTAINERS[2]['id']
ITEMS[5]['container_id'] = CONTAINERS[2]['id']


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/containers', methods=['GET'])
def all_containers():
    return jsonify({
        'status': 'success',
        'containers': CONTAINERS,
    })

@app.route('/new', methods=['POST'])
def new_container():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    CONTAINERS.append({
        'id': uuid.uuid4().hex,
        'name': post_data.get('name'),
        'items': []
    })
    response_object['message'] = 'Container added'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
