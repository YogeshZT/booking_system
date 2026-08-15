class UserAlreadyExists(Exception):
    pass

class AuthenticationError(Exception):
    pass

class EmailVerificationError(Exception):
    pass

class AlreadyVerifiedError(Exception):
    pass