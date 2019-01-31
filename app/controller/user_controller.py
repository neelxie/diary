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

        first_name = user_request.get("first_name")
        last_name = user_request.get("last_name")
        phone_number = user_request.get("phone_number")
        user_name = user_request.get("user_name")
        email = user_request.get("email")
        password = user_request.get("password")
        user_id = len(self.app_users.user_list) + 1

        error = self.validate_users.check_if_either_function_is_none(self.validate_users.validate_names(first_name, last_name, user_name), self.validate_users.validate_other(phone_number, email, password))

        if error:
            return jsonify({
                "status": 400,
                "error": error
            }), 400

        new_user = User(Base(first_name, last_name, phone_number, user_id), user_name, email, password)

        self.app_users.add_user(new_user)

        return jsonify({
            "status": 201,
            "success": [new_user.to_dict()]
        })


    def get_users(self):
        """
        Get all users.
        """
        users = self.app_users.get_user_list()

        if users is None:
            return jsonify({
                "status": 200,
                "data": ["No users yet."]
            }), 200

        return jsonify({
            "status": 200,
            "success": [user.to_dict() for user in users]
        }), 200


    def get_one_user(self, user_id):
        """
        Get single user by ID.
        """
        user = self.app_users.get_single_user(user_id)

        if user is None:
            return jsonify({
                "status": 400,
                "error": "No user by that ID."
            }), 400

        return jsonify({
            "status": 200,
            "success": [user.to_dict()]
        }), 200
        