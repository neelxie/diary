""" user models file."""
from datetime import datetime

class Base:

    def __init__(self, first_name, last_name, phone_number, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.user_id = user_id


class User:

    def __init__(self, base, user_name, email, password):
        self.base = base
        self.user_name = user_name
        self.email = email
        self.password = password
        self.created_on = str(datetime.now())


    
    def to_dict(self):
        return {
            "first_name": self.base.first_name,
            "last_name": self.base.last_name,
            "phone_number": self.base.phone_number,
            "user_id": self.base.user_id,
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password,
            "created_on": self.created_on
        }
    
class UserDB:
    """
    class for storing entries.
    """
    def __init__(self):
        """
        data structure to store users.
        """
        self.user_list = []

    def get_user_list(self):
        """
        retrieve all users in list
        """
        return self.user_list

    def get_single_user(self, user_id):
        """
        fetch single user by ID.
        """
        for user in self.user_list:
            if user.user_id == user_id:
               return user

    def add_user(self, user):
        """
        add user to users list.
        """
        self.user_list.append(user)