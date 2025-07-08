#essa sera a classe abstrata, resolvi criar ela para que houvesse herança 
#entre client e crew_member, pois compartilhavam os mesmo atributos
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, cpf: str):
        self._name = name
        self._cpf = cpf

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cpf(self):
        return self._cpf 

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @abstractmethod
    def show_info(self):
        pass