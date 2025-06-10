import pandas

HOTELS_LIST_FILEPATH = "hotels.csv"

df_hotels = pandas.read_csv(HOTELS_LIST_FILEPATH)


class Hotel:
    def __init__(self, id_hotel):
        pass

    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


if __name__ == "__main__":
    print(df_hotels)
    id_hotel = input("Enter the ID of the hotel: ")
    hotel = Hotel(id_hotel)

    if hotel.available():
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(name, hotel)
        reservation_ticket.generate()
    else:
        print("The hotel is not free")