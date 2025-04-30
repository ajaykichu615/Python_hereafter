# Create a class named MovieTicket to simulate a simple movie ticket booking system.
# Attributes:
# movie_name: Name of the movie.
# total_seats: Total number of seats available in the theatre.
# booked_seats: Number of seats already booked (initially 0).
# price_per_ticket: Price of one ticket.
#
# Methods:
# 1. book_ticket(num_seats)
# Books the given number of seats if available.
# If enough seats are available, update booked_seats and return the total cost.
# If not enough seats, display how many seats are left.
#
# 2. cancel_ticket(num_seats)
# Cancels the given number of booked tickets if that many were previously booked.
# Updates booked_seats accordingly.
# If trying to cancel more seats than booked, show an error.
#
# 3. check_availability()
# Returns the number of available seats.
#
# 4. show_details()
# Displays movie name, total seats, booked seats, available seats, and price per ticket.

import random
class MovieTicket:
    def __init__(self,movie_name,total_seats,booked_seats,price_per_ticket):
        self.movie_name=movie_name
        self.total_seats=500
        self.booked_seats=booked_seats
        self.price_per_ticket = 150

    def book_ticket(self,num_seats):
        while 0<self.total_seats<=500:
            num_seats = int(input('Enter the number of the seats that needs to be booked:'))
            if num_seats<=self.total_seats:
                self.total_seats -= num_seats
                print('Seats have been booked successfully')
                print(f'Total Cost = {150*num_seats}')
                break
            elif num_seats == 0 or not num_seats.isdigit():
                print('Enter a valid number')
            else:
                print(f'Not enough seats. Only {self.total_seats} are left')

    def cancel_ticket(self,num_seats):
        while 0<self.total_seats<=500:
            num_seats = int(input('Enter the number of seats that needs to be cancelled: '))
            if num_seats<=self.total_seats:
                self.total_seats += num_seats
                print('Seats have been cancelled successfully')
                print(f'Total seats left: {self.total_seats}')
                break
            elif num_seats == 0 or not num_seats.isdigit():
                print('Enter a valid number')




    def check_availability(self):
        return self.total_seats

    def show_details(self):
        print(self.movie_name)
        print(self.total_seats)
        print()

