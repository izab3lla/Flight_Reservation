from client import Client


class Seat:
    def __init__(self, seat_number: str, client: Client):
        self.seat_number = seat_number
        self.client = Client

    def get_seat_number(self):
        return self.seat_number

    def set_seat_number(self, value):
        self.seat_number = value

    def get_client(self):
        return self.client

    def set_client(self, value):
        self.client = value

