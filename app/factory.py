import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    cur_dir = os.getcwd()
    app.config['MODEL_PATH'] = os.path.join(cur_dir, 'app', 'data', 'model.pkl')

    return app