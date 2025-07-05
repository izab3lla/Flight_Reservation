import uuid
from crew_member import Crew
from seat import Seat


class Flight:
    def __init__(self, id_flight: str, price: float, seat: Seat, crew: Crew):
        self.__id_flight = str(uuid.uuid4()) #talvez gerar com uuid mas colocar no maximo 5 digitos para n ficar extenso
        self._price = price
        self.seat = seat
        self.crew = crew
    
    def add_crew_members(self):
        pass

    def reserve_seat(self):
        pass

    def show_seats(self):
        pass

    def shoe_crew(self):
        pass