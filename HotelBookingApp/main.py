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


class SpaHotel(Hotel):
    def book_spa_package(self):
        """ Book a spa package (currently no checks are implemented) """
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        """ Generate the hotel reservation ticket """
        content = f"""
        Thank you for your Hotel reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel_object.hotel_name}
        """
        return content


class SpaReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        """ Generate the spa reservation ticket """
        content = f"""
        Thank you for your Spa reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel_object.hotel_name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        """ Check if the provided credit card is valid """
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        """ Check if the secure authentication for using the credit card is valid """
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


if __name__ == "__main__":
    print("List of hotels:\n", df_hotels)

    hotel_id = input("Enter the ID of the hotel: ")
    hotel = SpaHotel(hotel_id)

    # Check hotel availability
    if hotel.available():
        # Check credit card validity and secure authentication validity
        credit_card = SecureCreditCard(number="1234")
        if credit_card.validate(expiration="12/26",
                                holder="JOHN SMITH",
                                cvc="123"):
            if credit_card.authenticate(given_password="mypass"):
                # Book the hotel
                hotel.book()

                # Generate the hotel reservation ticket
                name = input("Enter your name: ")
                reservation_ticket = ReservationTicket(name, hotel)
                print(reservation_ticket.generate())

                # Check the desire to book also a spa package
                spa_option = input("Do you want to book also a spa package? (yes/no) ")
                if spa_option == "yes":
                    # Book the spa package
                    hotel.book_spa_package()

                    # Generate the spa reservation ticket
                    spa_ticket = SpaReservationTicket(name, hotel)
                    print(spa_ticket.generate())
                else:
                    print("No spa package booked")
            else:
                print("Credit card authentication failed")
        else:
            print("Credit card validation failed")
    else:
        print("The hotel is not free")