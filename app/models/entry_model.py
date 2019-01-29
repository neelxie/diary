""" Models file for diary entry."""
from datetime import datetime

class Entry:
    """
    class for dairy entry.
    """
    def __init__(self, comment, author, entry_id):
        self.comment = comment
        self.author = author
        self.entry_id = entry_id
        self.registered = str(datetime.now())

    def to_json(self):
        return {
            "entry_id": self.entry_id,
            "author": self.author,
            "comment": self.comment,
            "created_on": self.registered
        }

class EntryDB:
    """
    class for storing entries.
    """
    def __init__(self):
        self.diary = []

    def get_diary(self):
        """
        fetch all entries in diary
        """
        return self.diary

    def get_single_entry(self, entry_id):
        """
        retrieve a single entry.
        """
        for entry in self.diary:
            if entry.entry_id == entry_id:
               return entry

    def remove_entry(self, entry_id):
        """
        delete diary entry
        """
        del self.diary[entry_id - 1]

    def add_entry(self, entry):
        """
        add entry to diary.
        """
        self.diary.append(entry)
