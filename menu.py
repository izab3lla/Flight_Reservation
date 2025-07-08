from client import Client
from crew_member import Crew
from flight import Flight
from faker import Faker

fake = Faker()
#os voo foram criados aqui mas os ids mudam com uuid por isso no prompt fica diferente
#são criados 10 voos com id diferentes
flights = [
    Flight("FLIGHT01", 350.00), #aqui ficou voo01 e o valor dele 
    Flight("FLIGHT02", 420.50),
    Flight("FLIGHT03", 289.90),
    Flight("FLIGHT04", 560.00),
    Flight("FLIGHT05", 610.75),
    Flight("FLIGHT06", 455.20),
    Flight("FLIGHT07", 380.40),
    Flight("FLIGHT08", 499.99),
    Flight("FLIGHT09", 525.30),
    Flight("FLIGHT10", 470.00),
]

for flight in flights: #isso foi algo novo mas precisei fazer para poder usar os nomes falsos 
    #com a faker mas ele roda em cada um dos 250 assentos e coloca o cliente la, com nome 
    for seat_num in range(1, 251):
        client_name = fake.name()
        fake_cpf = fake.ssn()
        fake_client = Client(client_name, fake_cpf)
        
        seat = flight._seats[seat_num - 1]  
        seat.client = fake_client  
        
def generate_crew_members(quantity=3): #aqui também precisei gerar cada membro da tripulação
    #são gerado os nomes e o cargo de cada um, resolvi forçar para aparecer apenas 
    #piloto, co-piloto e atendente, pois estava gerando alguns aleatorios e n era cabivel

    roles = ["Pilot", "Co-pilot", "Flight Attendant"]
    crew_members = []
    for i in range(quantity):
        name = fake.name()
        cpf = fake.ssn()
        role = roles[i % len(roles)]
        crew_members.append(Crew(name, role, cpf))
    return crew_members


for flight in flights:
    crew = generate_crew_members()
    for member in crew:
        flight.add_crew_member(member)


while True: #menu simples apenas duas opções, achei que ficaria melhor para poder aparecer o id do avião e poder acessar por ele
    #como são gerados aleatorios ajuda a fazer a pesquisa para não se perder
    print("\n=== FLIGHT RESERVATION MENU ===")
    print("1. List Flights")
    print("2. Flight Details")
    print("0. Exit")
    option = input("Choose: ")

    if option == '1':
        for flight in flights:
            print(f"ID: {flight.id_flight}")

    elif option == '2':
        flight_id = input("Flight ID: ").strip()
        flight = next((f for f in flights if f.id_flight == flight_id), None)
        if flight:
            print(f"\nFlight {flight.id_flight} | Price: ${flight.price}")
            print("Crew:")
            flight.show_crew()
            print("\nRandom Seats:")
            flight.show_seats()
        else:
            print("Flight not found.")

    elif option == '0':
        break

    else:
        print("Invalid option. Please try again.")
