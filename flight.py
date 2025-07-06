import uuid
from crew_member import Crew
from seat import Seat


class Flight:
    def __init__(self, id_flight: str, price: float, seat: Seat, crew: Crew):
        self.__id_flight = str(uuid.uuid4()) #talvez gerar com uuid mas colocar no maximo 5 digitos para n ficar extenso
        self._price = price
        self.seat = seat
        self.crew = crew
    

    @property
    def _id_flight(self):
        return self.__id_flight

    @_id_flight.setter
    def _id_flight(self, value):
        self.__id_flight = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def get_seat(self):
        return self.seat

    def set_seat(self, value):
        self.seat = value

    def get_crew(self):
        return self.crew

    def set_crew(self, value):
        self.crew = value

    def add_crew_members(self):
        pass

    def reserve_seat(self):
        pass

    def show_seats(self):
        pass

    def shoe_crew(self):
        pass