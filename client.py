#dividido em files 
# client -> voo -> lugar
# tripulantes -> voo

class Client:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
