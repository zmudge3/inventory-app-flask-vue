from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

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
    return jsonify({
        'status': 'success',
        'containers': CONTAINERS,
    })

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


if __name__ == '__main__':
    app.run()
