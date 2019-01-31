""" users view file."""
from flask import Blueprint
from ..controller.user_controller import User_Controller

user_controller = User_Controller()

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route('/signup', methods=['POST'])
def sign_up():
    """ 
    register up as app user
    """
    return user_controller.add_user()

@auth_bp.route('/users', methods=['GET'])
def fetch_all_users():
    """
    admin route to get all users
    """
    return user_controller.get_users()

@auth_bp.route('/users/<int:user_id>', methods=['GET'])
def fetch_one_user(user_id):
    """
    get single user by ID.
    """
    return user_controller.get_one_user(user_id)