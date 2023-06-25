# lets extend Exception class to create our own exception class.

# Path: src/exceptions/invalid_db_type.py

class InvalidDBType(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
