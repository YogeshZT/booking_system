from exceptions.app_exception import AppException


class CannotCreateRoomError(AppException):
    def __init__(self):
        super().__init__(
            message = "Cannot create room",
            status_code = 400
        )


class CannotEditRoomError(AppException):
    def __init__(self):
        super().__init__(
            message = "Cannot edit room details",
            status_code = 400
        )


class CannotFetchRoomDetailsError(AppException):
    def __init__(self):
        super().__init__(
            message = "Cannot fetch room details",
            status_code = 400
        )


class CannotBlockRoomError(AppException):
    def __init__(self):
        super().__init__(
            message = "Cannot block room",
            status_code = 400
        )

class CannotUnblockRoomError(AppException):
    def __init__(self):
        super().__init__(
            message = "Cannot unblock room",
            status_code = 400
        )