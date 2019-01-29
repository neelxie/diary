""" validation class file."""

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