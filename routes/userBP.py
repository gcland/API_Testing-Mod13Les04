from flask import Blueprint
from controllers.userController import get, login

user_blueprint = Blueprint('user_bp', __name__)
user_blueprint.route('/', methods=['GET'])(get)
user_blueprint.route('/login', methods=['POST'])(login)
