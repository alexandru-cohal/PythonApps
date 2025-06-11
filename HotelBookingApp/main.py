import pandas

HOTELS_LIST_FILEPATH = "hotels.csv"
CARDS_LIST_FILEPATH = "cards.csv"
CARDS_SECURITY_LIST_FILEPATH = "card_security.csv"

df_hotels = pandas.read_csv(HOTELS_LIST_FILEPATH, dtype={"id": str})
df_cards = pandas.read_csv(CARDS_LIST_FILEPATH, dtype="str").to_dict(orient="records")
df_cards_security = pandas.read_csv(CARDS_SECURITY_LIST_FILEPATH, dtype="str")


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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


if __name__ == "__main__":
    print(df_hotels)
    hotel_id = input("Enter the ID of the hotel: ")
    hotel = Hotel(hotel_id)

    if hotel.available():
        credit_card = SecureCreditCard(number="1234")
        if credit_card.validate(expiration="12/26",
                                holder="JOHN SMITH",
                                cvc="123"):
            if credit_card.authenticate(given_password="mypass"):
                hotel.book()
                name = input("Enter your name: ")
                reservation_ticket = ReservationTicket(name, hotel)
                print(reservation_ticket.generate())
            else:
                print("Credit card authentication failed")
        else:
            print("There was a problem with the credit card")
    else:
        print("The hotel is not free")