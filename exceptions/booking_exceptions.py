from exceptions.app_exception import AppException


class RoomNotAvailableError(AppException):
    def __init__(self):
        super().__init__(
            message="Room is unavailable or doesn't exist",
            status_code = 404
        )

class CannotCreateBookingError(AppException):
    def __init__(self):
        super().__init__(
            message = "Cannot create booking, try again after some time",
            status_code = 400
        )
