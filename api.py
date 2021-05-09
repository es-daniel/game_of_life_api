import flask
from flask_cors import CORS
from utils import Utils
import json
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

utils = Utils()


@app.route('/start', methods=['GET'])
def start():
    grid = utils.build_new_grid()
    utils.seed(grid)
    save_grid(grid)
    return jsonify(grid)


@app.route('/update', methods=['GET'])
def update():
    current_grid = read_grid()
    new_grid = utils.update_grid(current_grid)
    save_grid(new_grid)
    return jsonify(new_grid)


def save_grid(grid):
    db = open('history.json', 'w')
    db.write(json.dumps(grid))
    db.close()

def read_grid():
    grid = open('history.json')
    return json.load(grid)


app.run()
