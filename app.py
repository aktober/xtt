from flask import Flask, render_template
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import SQLALCHEMY_DATABASE_URI


app = Flask(__name__, static_url_path='')
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from operations import models
migrate = Migrate(app, db)

from resources.grab_and_save import GrabSaveResource
from resources.last import LastResource

api.add_resource(LastResource, '/api/v1/last/')
api.add_resource(GrabSaveResource, '/api/v1/grab_and_save/')


@app.route('/')
def index():
    return "Xapo test task"


@app.route('/last')
def last_view():
    return render_template('layout.html')


@app.route('/vue-last')
def vue_last_view():
    return render_template('vue_layout.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
