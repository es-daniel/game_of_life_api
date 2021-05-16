import flask
from flask_cors import CORS
from utils import Utils
import json
from flask import request, jsonify

app = flask.Flask(__name__)
CORS(app)

utils = Utils()


# This is the home end point
@app.route('/', methods=['GET'])
def home():
    return "<b>Game of life API</b>"


# This is the end pint to start the game
@app.route('/start', methods=['GET'])
def start():
    pattern = request.args.get('pattern')
    grid = []
    print(pattern)
    if pattern == 'rand':
        grid = utils.build_new_grid(20, 25)  # 20 rows with 25 columns
        utils.seed(grid)
    elif pattern == 'gosper_glider_gun':
        grid = utils.gosper_glider_gun()
    elif pattern == 'pulsar':
        grid = utils.pulsar()
    save_grid(grid)
    return jsonify(grid)


# This is the end point to update the game
@app.route('/update', methods=['GET'])
def update():
    current_grid = read_grid()
    new_grid = utils.update_grid(current_grid)
    save_grid(new_grid)
    return jsonify(new_grid)


# This save the current grid in the server
def save_grid(grid):
    db = open('history.json', 'w')
    db.write(json.dumps(grid))
    db.close()


# This method load the current grid saved in the server
def read_grid():
    grid = open('history.json')
    return json.load(grid)

# This statement runs the app
if __name__ == '__main__':
    app.run()
