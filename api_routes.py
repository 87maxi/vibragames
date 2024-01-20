from controllers.user_api import index, create, delete, get_user
from flask import Blueprint


######### api

api_v1 = Blueprint('api_v1', __name__)

api_v1.route('', methods=['GET'])(index)
api_v1.route('', methods=['POST'])(create)
api_v1.route('/delete', methods=['POST'])(delete)
api_v1.route('/get_user', methods=['POST'])(get_user)