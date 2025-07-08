 #I will put the creation of seats and also the flight here
from flight import Flight
from seat import Seat

def create_seats(num):  # I will create the 250 seats here, I think it makes sense
    return [Seat(number=i) for i in range(num)]

