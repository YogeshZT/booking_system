class AppException(Exception):
    def __init__(self, message : str, status_code : int =400):
        self.message = message
        self.status_code = status_code


class UserAlreadyExists(AppException):
    def __init__(self):
        super().__init__("User already exists", 400)


class AuthenticationError(AppException):
    def __init__(self):
        super().__init__("Unauthorized", 404)


class EmailVerificationError(AppException):
    def __init__(self):
        super().__init__("Can't verify email, please try again", 404)


class AlreadyVerifiedError(AppException):
    def __init__(self):
        super().__init__("Unauthorized", 404)

