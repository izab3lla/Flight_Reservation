import random
import uuid
from client import Client
from crew_member import Crew
from seat import Seat


class Flight:
    def __init__(self, id_flight: str, price: float, seat: Seat, crew: Crew):
        self._id_flight = str(uuid.uuid4()) [:5]#talvez gerar com uuid mas colocar no maximo 5 digitos para n ficar extenso
        self._price = price #o preco
        self._seats = [Seat(number=i) for i in range(250)]
        self._crew = [] #listado a partir da classe de tripulantes
    

    @property
    def _id_flight(self):
        return self._id_flight

    @_id_flight.setter
    def _id_flight(self, value):
        self._id_flight = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def get_seat(self):
        return self._seat

    def set_seat(self, value):
        self._seat = value

    def get_crew(self):
        return self._crew

    def set_crew(self, value):
        self._crew = value

    def add_crew_members(self, crew_member: Crew):
        #vou apenas adicionar um lista com append
        self._crew.append(crew_member)

    def reserve_seat(self, number_seat: int, client: Client):
        #aqui vou precisar fazer verificação se o lugar ta vago e está no limite de 250, talvez fazer try 
        if not (0 <= number_seat < 250): 
            raise ValueError ("Numero de assento invalido!")
        self.seats[number_seat].reserve(client)
        

    def show_seats(self):
        '''a logica entre os dois vai ser a mesma
        vou usar o random pra poder printar os assentos
        usando indices de 0 até 250, assim vão ficar aleatorios
        dentro do que foi pedido'''

        sample = random.sample(self.seats, 10)
        for seat in sample:
            if seat.is_reserved:
                print(f"Assento {seat.number} está ocupado por {seat.client.nome}")
            else:
                print(f"Assento {seat.number} está livre.")

    def show_crew(self):
        for member in self._crew:
            print(f"{member.name}, {member.role}")