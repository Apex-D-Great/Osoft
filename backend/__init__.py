from flask import Flask, jsonify
from flask_restx import Api, Resource
from flask_jwt_extended import JWTManager
from .models import db
from .configurations.config import DevConfig
from flask_migrate import Migrate
from flask_cors import CORS
import os

from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config.from_object(DevConfig)
api = Api(app, doc="/docs")
app.config['SERVER_NAME'] = 'localhost:5000'

CORS(app)
JWTManager(app)

# db_init
db.init_app(app)
app.app_context().push()
db.create_all()

migrate = Migrate(app,db)
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

# oauth = OAuth(app)

from .routes.auth import auth_ns
from .routes.product import product_ns

# api.add_namespace(recipe_ns)
api.add_namespace(auth_ns)
api.add_namespace(product_ns)




@app.shell_context_processor
def make_shell_context():
    return {"db":db}

