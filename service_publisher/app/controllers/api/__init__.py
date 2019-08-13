from flask import Blueprint
from flask_restful import Api
from .health import *
from .email import *

api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint)

api.add_resource(HealthCheck, "/health")
api.add_resource(SendEmail, "/email")



