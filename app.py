from flask import Flask
from flask_restful import Api

import certs_resources
from data import db_session

app = Flask(__name__)
api = Api(app)

app.config['DATABASE_FILE'] = "db/database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.config["DATABASE_FILE"]}?check_same_thread=False'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'very_secret_key'
db_session.global_init("db/database.db")

api.add_resource(certs_resources.CertsListResource, '/api/v1/certs')
api.add_resource(certs_resources.CertResource, '/api/v1/certs/<int:cert_id>')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
