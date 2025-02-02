from backend.helpers import *


class InsufficientData(ExplainableException):
    pass


class AlreadyExists(ExplainableException):
    pass


class NotFound(ExplainableException):
    def status(self):
        return 404


class IncorrectPassword(ExplainableException):
    pass

class IncorrectDays(ExplainableException):
    pass

class IncorrectEmail(ExplainableException):
    pass

class IncorrectBirthday(ExplainableException):
    pass


class IncorrectToken(ExplainableException):
    pass


class NotInProject(ExplainableException):
    pass


class ExpiredToken(ExplainableException):
    pass


class NoToken(ExplainableException):
    def status(self):
        return 403


class AccessDenied(ExplainableException):
    def status(self):
        return 403

class MedsengerAlreadyExists(ExplainableException):
    pass