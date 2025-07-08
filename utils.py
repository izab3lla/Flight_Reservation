#vou colocar a criação de lugares e também do voo aqui
from seat import Seat


def create_seats(num): #vou criar os 250 lugares aqui, acho que faz sentido
        return [Seat(number = i) for i in range(num)]

def creat_voo(flights):
        pass