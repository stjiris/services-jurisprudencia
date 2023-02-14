from flask import Flask
from flask_cors import CORS
from procs_mentioned import searchProcs
import os


app = Flask(__name__)
CORS(app)

@app.route('/mentioned/<path:proc>/<uuid>/', methods=['GET'])
def related(proc=None, uuid=None):
    return searchProcs(proc, uuid)

if __name__ == "__main__":
    host=app.run(host=os.environ.get("FLASK_SERVER_ADDRESS", '127.0.0.1'), port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=False)