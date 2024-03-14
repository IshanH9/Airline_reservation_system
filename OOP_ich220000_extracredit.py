#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Flight:
    def __init__(self, capacity, fare):
        self.capacity = capacity
        self.available_seats = capacity
        self.fare = fare

    def check_availability(self):
        return self.available_seats

    def book_seat(self, num_seats):
        if num_seats <= 0:
            print("Please enter a valid number of seats.")
            return False

        if num_seats <= self.available_seats:
            self.available_seats -= num_seats
            return True
        else:
            print("Sorry, not enough seats available.")
            return False

    def cancel_booking(self, num_seats):
        if num_seats <= 0:
            print("Please enter a valid number of seats.")
            return False

        if self.capacity - self.available_seats + num_seats <= self.capacity:
            self.available_seats += num_seats
            print("Booking canceled successfully.")
            return True
        else:
            print("Invalid number of seats to cancel.")
            return False

    def amount_due(self, num_seats):
        return num_seats * self.fare


def display_options():
    print("Available Flight Options:")
    print("1. Flight A (50 seats) - Fare: $100")
    print("2. Flight B (30 seats) - Fare: $150")
    print("3. Flight C (40 seats) - Fare: $120")


if __name__ == "__main__":
    flights = [Flight(50, 100), Flight(30, 150), Flight(40, 120)]

    while True:
        display_options()
        choice = input("Select a flight option (1-3) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting the reservation system. Goodbye!")
            break

        try:
            choice = int(choice)
            if 1 <= choice <= 3:
                selected_flight = flights[choice - 1]
                available_seats = selected_flight.check_availability()

                print(f"\nFlight {chr(64 + choice)} - Available seats: {available_seats}")

                action = input("Do you want to book (b), cancel (c), or go back (q)? ").lower()

                if action == 'b':
                    num_seats = int(input("Enter the number of seats to book: "))
                    if selected_flight.book_seat(num_seats):
                        print(f"Booking successful! Amount due: ${selected_flight.amount_due(num_seats)}")
                elif action == 'c':
                    num_seats = int(input("Enter the number of seats to cancel: "))
                    selected_flight.cancel_booking(num_seats)

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


# In[ ]:





# In[ ]:




