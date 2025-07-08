# Divided into files
# client -> flight -> seat
# crew -> flight
from person import Person

class Client(Person):
    def __init__(self, name: str, cpf: str):
        super().__init__(name, cpf)  #foram usados os atributos de outra classe 

    def show_info(self): #apenas printa o nome e o cpf do cliente
        print(f"Client: {self.name}, CPF: {self.cpf}")
