from flask import Flask
from flask_cors import CORS
from . import configs
from app.libs import kafka_libs

producer = kafka_libs.get_producer()

def create_app():
    app = Flask(__name__)
    app.config.from_object(configs.Config)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .controllers import api_blueprint

    app.register_blueprint(api_blueprint)
    
    return app