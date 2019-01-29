""" user controller file."""

from flask import request, jsonify
from ..models.user_model import User, Base, UserDB
from ..utils.validation import Validation

class User_Controller:
    """
    App users controller class.
    """
    app_users = UserDB()
    validate_users = Validation()

    def add_user(self):
        """
        add app user.
        """
        user_request = request.get_json()

        user_attributes = ["first_name", "last_name", "phone_number", "user_name", "email", "password"]

        error_list = self.validate_users.validate_attribute(user_request, user_attributes)

        if error_list:
            return jsonify({
                "status": 400,
                "error": error_list,
                "missing": "This/These attributes are missing."
            }), 400

        