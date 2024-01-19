from controllers.user_api import index
from flask import Blueprint


######### api

api_v1 = Blueprint('api_v1', __name__)

api_v1.route('/', methods=['GET'])(index)
