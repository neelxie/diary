""" entry view file."""
from flask import Blueprint
from ..controller.entry_controller import Entry_Controller


entry_controller = Entry_Controller()

entry_bp = Blueprint('entry_bp', __name__)

@entry_bp.route('/entries', methods=['POST'])
def add_entry():
    """
    add entry to diary.
    """
    return entry_controller.add_entry()

@entry_bp.route('/entries', methods=['GET'])
def fetch_all_entries():
    """
    admin route to get all diary entry.
    """
    return entry_controller.get_entries()

@entry_bp.route('/entries/<int:entry_id>', methods=['GET'])
def get_single_entry(entry_id):
    """
    fetch single entry
    """
    return entry_controller.get_one_entry(entry_id)

@entry_bp.route('/entries/<int:entry_id>')
def modify_entry(entry_id):
    """
    modify single entry
    """
    return entry_controller.modify_entry(entry_id)