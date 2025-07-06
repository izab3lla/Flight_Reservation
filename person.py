#classe abstrata, sera usada tanto em client quando em crew havendo herança entre ambos
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, cpf: str):
        self._name = name
        self.__cpf = cpf

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @abstractmethod
    def show_info(self):
        pass