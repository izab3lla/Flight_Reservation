class Crew:
    def __init__(self, name: str, role: str):
        self._name = name
        self._role = role

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
 #como nenhum dado presente é sensivel estou adicionando apenas como protegido