import datetime
class Property:
    def __init__(self, property_id, name, location, description, price_per_night, availability_status=True):
        self.property_id = property_id
        self.name = name
        self.location = location
        self.description = description
        self.price_per_night = price_per_night
        self.availability_status = availability_status

    def is_available(self):
        return self.availability_status

    def update_availability(self, status):
        self.availability_status = status


class User:
    def __init__(self, user_id, name, contact_details):
        self.user_id = user_id
        self.name = name
        self.contact_details = contact_details


class Host(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.properties = []

    def list_property(self, property):
        self.properties.append(property)


class Guest(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.bookings = []

    def book_property(self, property, check_in_date, check_out_date):
        if property.is_available():
            booking = Booking(property, self, check_in_date, check_out_date)
            self.bookings.append(booking)
            property.update_availability(False)
            return booking
        else:
            return None


class Booking:
    def __init__(self, property, guest, check_in_date, check_out_date, booking_status="confirmed"):
        self.property = property
        self.guest = guest
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.booking_status = booking_status


class overall_review:
    def __init__(self, property, guest, rating, comment):
        self.property = property
        self.guest = guest
        self.rating = rating
        self.comment = comment

class User:
    def __init__(self, user_id, name, contact_details):
        self.user_id = user_id
        self.name = name
        self.contact_details = contact_details

class Host(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.properties = []

    def list_property(self, property):
        self.properties.append(property)

class Guest(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.bookings = []

    def book_property(self, property, check_in_date, check_out_date):
        booking = Booking(property, self, check_in_date, check_out_date)
        self.bookings.append(booking)
        property.update_availability(check_in_date, check_out_date)

class Property:
    def __init__(self, property_id, name, location, description, price_per_night):
        self.property_id = property_id
        self.name = name
        self.location = location
        self.description = description
        self.price_per_night = price_per_night
        self.availability = True

    def update_availability(self, check_in_date, check_out_date):
        pass

class Booking:
    def __init__(self, property, guest, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.property = property
        self.guest = guest
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = "confirmed"

    def cancel_booking(self):
        self.status = "canceled"
        self.property.update_availability(self.check_in_date, self.check_out_date)




host1 = Host("1", "Naqvi","naqvi@example.com")
guest1 = Guest("101", "uzi", "uzi@example.com")
property1 = Property("P1", "Cozy Huge Cottage", "New York", "A cozy cottage in New York", 100)
property2 = Property("P2", "Luxury Apartment", "Islamabad", "A luxury apartment in Islamabad", 200)
host1.list_property(property1)
host1.list_property(property2)
