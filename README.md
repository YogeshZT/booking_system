BOOKING SYSTEM

REQUIREMENTS
Functional
User Related
User can login
User can logout
User can signup/register
User can see available rooms along with booked and empty slots
Room Related
Admins can create a room
Admin can delete a room 
Admin can block a room for a particular time frame
Users can see list of room
User can see existing booking for a room
Booking related
Bookings are created by the user for an empty slot
User can cancel a booked meeting
User can see their previous and upcoming bookings
User can see booked time slot for a room but can’t book them
Non-Functional
Everything should be robust enough to enhance functionalities
Authentication and authorization
Two users must never book the same time slot of a room
Passwords shouldn’t be stored as plain text
Admin APIs require admin privilege
Users can only cancel their own bookings


ACTORS AND PERMISSiONS
Users
Should be able to navigate the front end
Able to see available rooms
Able to book available rooms
Cancel any own booking they have
They should not be able to perform admin only operations
Admins
All permissions which users have
Configuration access for the rooms which allows them to:
Change state of any existing room
Add new rooms with specific configuration
Add new admins i.e a new admin can only be added by an existing admin

BUSINESS RULES
A user can have at most 2 active bookings.
A booking must use exactly one room and one predefined slot.
A room cannot have overlapping active bookings.
Users cannot book blocked slots.
Blocked slots are visible but unavailable to users.
Users can cancel only their own bookings.
Cancelled bookings don’t count toward the active-booking limit.
Bookings cannot be modified after creation.
Users cannot book beyond the configured advance-booking period.
Only active rooms can be booked.
Only authenticated and verified users can create bookings.
Only admins can create rooms and blocks.
Only an existing admin can create another admin.
Admins cannot remove the last remaining admin.
A room block cannot overlap an existing booking.
A booking cannot be created in the past.
A booking’s duration must equal the configured slot duration.
Concurrent attempts to reserve the same room/slot must result in at most one successful booking.

APIs AND API CONTRACTS
Note: General response format will be : message(string), response(json)
Auth and login apis:
POST api/v1/auth/login - for logging in a user
Request body: email : string, password : string
Response:{email, name}
POST api/v1/auth/logout - for logging out a user
Request body: …
Response: …
POST api/v1/auth/signup - for onboarding a new user
Request body: {name, email, password}
Response: {user_id}
POST api/v1/auth/verify-email
Request body: {verification_token}
Response: …
POST api/v1/auth/resend-verification
Request: {email}
POST api/v1/auth/forgot-password
Request body: {email}
Post api/v1/auth/reset-password
Request body: {reset_token, new_password}
NOTE: All of these are for user roles
Booking apis
POST api/v1/bookings - for creating a booking
Request: {room_id, start_time}
Response: {booking_id, room_id, start_time, end_time}
GET api/v1/bookings/me - for getting all of the users bookings data (user specific checks)
Request:....
Response: list of {booking_id, room_id, room_name, start_time, end_time, status}
GET api/v1/bookings/{booking_id} - booking specific detail
Request body: …
Response: {booking_id, room_id, room_name, start_time, end_time, status}
DELETE api/v1/bookings/{booking_id} - delete or cancel a booking(user specific checks)
Request body:...
Response : {booking_id, status}
NOTE: 1 and 2 are for user roles while 3 is for both user and admin
Room apis:
GET api/v1/rooms/ : get all rooms
Request body:
Response: list of {room_id, room_name, status}
GET api/v1/rooms/{room_id} : get a particular room’s details
Request body: …
Response: {room_id, room_name, status}
GET api/v1/rooms/{room_id}/availability?date : get rooms available on a particular date
Request body: …
Response : {room_id, room_name, status}
POST api/v1/rooms/: creating a room (Admin only)
Request body : {room_name}
Response : {room_id, name, status}
PATCH api/v1/rooms/:making changes to a room’s configurations
Request body : {room_name}
POST api/v1/rooms/block/: for blocking a room (making it unavailable) (admin only)
DELETE api/v1/rooms/block/: removing a blocked room (admin only)
