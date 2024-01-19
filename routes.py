from controllers.user import index, create, insert

from flask import Blueprint


blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['POST'])(create)
blueprint.route('/insert', methods=['GET'])(insert)