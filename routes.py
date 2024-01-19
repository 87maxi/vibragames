from controllers.user import index, create, edit, update, delete

from flask import Blueprint


blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['POST'])(create)
blueprint.route('/edit/<int:id>/', methods=["GET"])(edit)
blueprint.route('/update/<int:id>/', methods=['POST'])(update)
blueprint.route('/delete/<int:idx>/', methods=['POST', 'GET' ])(delete)