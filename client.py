# Divided into files
# client -> flight -> seat
# crew -> flight
from person import Person

class Client(Person):
    def __init__(self, name: str, cpf: str):
        super().__init__(name, cpf)  # Here name and cpf are already set

    def show_info(self):
        print(f"Client: {self.name}, CPF: {self.cpf}")
