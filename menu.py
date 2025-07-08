#menu simples
from client import Client

while True:
        print("\n=== MENU DE RESERVA DE VOOS ===")
        print("1. Listar Voos")
        print("2. Reservar Assento")
        print("3. Detalhes do Voo")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            for i, voo in enumerate(flights, 1):
                print(f"{i}. ID: {voo.id_flight} | Preço: R${voo.price}")

        elif opcao == '2':
            idx = int(input("Nº do voo: ")) - 1
            nome = input("Nome do cliente: ")
            assento = int(input("Assento (1-250): ")) - 1
            try:
                flights[idx].reserve_seat(assento, Client(nome))
                print("Reserva feita!")
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == '3':
            idx = int(input("Nº do voo: ")) - 1
            voo = flights[idx]
            print(f"\nVoo {voo.id_flight} | R${voo.price}")
            print("Tripulação:")
            voo.show_crew()
            print("\nAssentos Aleatórios:")
            voo.show_seats()

        elif opcao == '0':
            break
        else:
            print("Ops,Opção inválida. Tente novamente")