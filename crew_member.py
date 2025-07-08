# Crew class with association
from person import Person

class Crew(Person):
    def __init__(self, name: str, role: str, cpf: str = ""):
        super().__init__(name, cpf)
        self._role = role  
    @property
    def role(self):
        return self._role  
    
    @role.setter
    def role(self, value):
        self._role = value 
    
    def show_info(self): #coloquei os show info em cada classe que precisava printar algo apenas para ir direto no menu
        print(f"Crew member: {self.name} | Role: {self.role}")
