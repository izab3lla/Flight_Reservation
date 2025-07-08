# Abstract class, will be used both in Client and Crew with inheritance between them
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, cpf: str):
        self._name = name
        self._cpf = cpf

    @property
    def name(self):
        return self._name  # access the actual attribute

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cpf(self):
        return self._cpf  # access the actual attribute

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @abstractmethod
    def show_info(self):
        pass