from exceptions.app_exception import AppException


class UserAlreadyExists(AppException):
    def __init__(self):
        super().__init__("User already exists", 400)


class AuthenticationError(AppException):
    def __init__(self):
        super().__init__("Unauthorized", 401)

class AuthorizationError(AppException):
    def __init__(self):
        super().__init__("Unauthorized", 403)


class EmailVerificationError(AppException):
    def __init__(self):
        super().__init__("Can't verify email, please try again", 400)


class AlreadyVerifiedError(AppException):
    def __init__(self):
        super().__init__("User already verified", 404)


class WrongPasswordError(AppException):
    def __init__(self):
        super().__init__("Wrong password entered", 401)

