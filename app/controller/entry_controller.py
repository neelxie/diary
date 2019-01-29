""" entry controller file."""
from flask import request, jsonify
from ..models.entry_model import Entry, EntryDB
from ..utils.validation import Validation

class Entry_Controller:
    """
    controller for the entry.
    """
    my_diary = EntryDB()
    valid = Validation()

    def add_entry(self):
        """
        add entry to diary.
        """
        data = request.get_json()

        entry_id = len(self.my_diary.diary) + 1
        author = data.get("author")
        comment = data.get("comment")

        entry_list = ['author', 'comment']
        error_attribute = self.valid.validate_attribute(data, entry_list)

        return jsonify({
            "status": 400,
            "error": error_attribute,
            "missing": "This/These attributes are missing."
        }), 400

        error = self.valid.validate_comment(comment)

        if error:
            return jsonify({
                "status": 400,
                "error": error
            })

        new_entry = Entry(comment, author, entry_id)
        self.my_diary.add_entry(new_entry)

        return jsonify({
            "status": 201,
            "success": new_entry.to_json()
        }), 201


    def get_entries(self):
        """
        get all entries.
        """
        if self.my_diary.diary is None or len(self.my_diary.diary) < 1:
            return jsonify({
                "status": 200,
                "message": "There are no entries so far."
            }), 200

        return jsonify({
            "status": 200,
            "all entries": [entry.to_json() for entry in self.my_diary.diary]
        }), 200


    def get_one_entry(self, entry_id):
        """
        get a single entry.
        """
        entry = self.my_diary.get_single_entry(entry_id)

        if entry is None:
            return jsonify({
                "status": 400,
                "error": "No entry by that ID."
            }), 400
        
        return jsonify({
            "status": 200,
            "success": [entry.to_json()]
        }), 200

    
    def modify_entry(self, entry_id):
        """
        modify entry
        """
        entry = self.my_diary.get_single_entry(entry_id)

        if entry is None:
            return jsonify({
                "status": 400,
                "error": "Can not modify non existant entry."
            }), 400

        data = request.get_json()
        new_comment = data.get("comment")

        error = self.valid.validate_comment(new_comment)

        if error:
            return jsonify({
                "status": 400,
                "error": error
            }), 400

        entry.comment = new_comment
        
        return jsonify({
            "status": 200,
            "success": [entry.to_json()]
        }), 200
