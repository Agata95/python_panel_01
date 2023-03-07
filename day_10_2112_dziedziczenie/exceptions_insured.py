class BadPeselNumber(Exception):
    """Raised when PESEL number will be different than 11 digit"""
    pass


class PeselNotNumber(Exception):
    """Raised when in PESEL will be string character non digit"""
    pass