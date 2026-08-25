from exceptions.app_exception import AppException


class CannotCreateRoomError(AppException):
    def __init__(self):
        super().__init__(
            message = "Cannot create room",
            status_code = 400
        )