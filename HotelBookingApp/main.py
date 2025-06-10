import pandas

HOTELS_LIST_FILEPATH = "hotels.csv"

df_hotels = pandas.read_csv(HOTELS_LIST_FILEPATH, dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df_hotels.loc[df_hotels["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """ Book a hotel by changing its availability """
        df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"] = "no"
        df_hotels.to_csv(HOTELS_LIST_FILEPATH, index = False)

    def available(self):
        """ Check if the hotel is available """
        availability = df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel_object.hotel_name}
        """
        return content


if __name__ == "__main__":
    print(df_hotels)
    hotel_id = input("Enter the ID of the hotel: ")
    hotel = Hotel(hotel_id)

    if hotel.available():
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(name, hotel)
        print(reservation_ticket.generate())
    else:
        print("The hotel is not free")