class BookingService:
    def __init__(self, booking_repository):
        self.booking_repository = booking_repository

    def create_booking(self, payload, user_id):
        pass

    def get_user_bookings(self, user_id):
        pass

    def get_booking_details(self, booking_id, user_id):
        pass

    def delete_booking(self, booking_id, user_id):
        pass