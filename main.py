
from flask import Flask , abort
from escrape import get_election_json
import json

app = Flask(__name__)


@app.route('/<pradesh>/<string:district>/<int:area>')
def index(pradesh,district,area):
    try:
        return json.dumps(get_election_json(pradesh,district,area))
    except:
        abort(404,"Invalid input")

if __name__ == "main":
    app.run(debug=True)