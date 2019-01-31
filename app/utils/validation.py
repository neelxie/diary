""" validation class file."""
import re

class Validation:
    """
    valdation class.
    """

    def validate_attribute(self, data, my_list):
        """
        validate attributes from request method.
        """
        if data is None or len(data) < 1:
            return "No data was entered."

        new_list = [attr for attr in my_list if data.get(attr) is None]

        if new_list > 0:
            return new_list
            

    def validate_comment(self, comment):
        """
        validate entry comment.
        """
        valid_comment = None

        if comment is None or isinstance(comment, str) is False:
            valid_comment = False

        if comment.isspace() or len(comment) < 9:
            valid_comment = False

        if valid_comment is False:
            return "Comment has to be a valid sentence."

    def check_for_spaces(self, word):
        """
        check for spaces amidst a word.
        """
        spaces = word.find(' ')
        if spaces is not -1:
            return False

    def validate_name(self, my_string):
        """
        check if name is valid.
        """
        if not isinstance(my_string, str) or my_string.isspace() or self.check_for_spaces(my_string) is False:
            return False

        if my_string.isalpha() is False  or len(my_string) > 15 or len(my_string) < 2:
            return False

    def validate_names(self, first_name, last_name, user_name):
        """
        check for valid names
        """
        error = None
        if self.validate_name(first_name) is False:
            error = "First name must be a string between 2 - 15 letters."

        if self.validate_name(last_name) is False:
            error = "Last name must be a string between 2 - 15 letters."

        if self.validate_name(user_name) is False:
            error = "Last name must be a string between 2 - 15 letters."

        return error


    def validate_other(self, phone_number, email, password):
        """
        validate phone number, email and password.
        """
        if not isinstance(email, str) or self.check_for_spaces(email) is False or not re.match(
                r"[^@.]+@[a-z]+\.[a-z]+", email):
            return "Enter a valid email address."

        if not isinstance(password, str) or len(password) < 6 or len(password) > 15:
            return "Password has have 6 to 15 characters."

        if len(phone_number) < 7 or isinstance(int(phone_number), int) is False:
            return "Phone number must be only digits and no white spaces."

    
    def check_if_either_function_is_none(self, func1, func2):
        """This function takes in two functions and checks if neither is none.
        """
        error_one = func1
        error_two = func2
        if error_one is not None:
            return error_one
        elif error_two is not None:
            return error_two
        return None