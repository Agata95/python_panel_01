class TooOldPerson(Exception):
    """Raised when year of birth is before 1900"""

    def __init__(self, message="Year of birth before 1900"):
        self.message = message
