class Parking_Garage:

    def __init__(self, tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket

    def EnterGarage(self):
        print("Welcome to the garage! You get to choose your own payment amount when you leave!")


    def TakeTicket(self):
        if self.tickets == []:
            print("Garage is full!")
            return
        if self.parking_spaces == []:
            print("Garage has no spaces available!")
            return
        self.tickets.pop()
        self.parking_spaces.pop()
        
        



    def Pay_for_Parking(self):
        parkingpayment= input("Type amount for your parking spot?: ")
        if parkingpayment != "":
            print("Your ticket has been paid and you have 15mins to leave!")
            self.current_ticket["paid"] = True


    
    def leave_garage(self):
        if self.current_ticket["paid"]:
            print("Thank you have a nice day!")
            self.tickets.append(1)
            self.parking_spaces.append(1)
        else:
            self.Pay_for_Parking()
            self.leave_garage()
            
        
    def main(self):
        while True:
            print("1. Take Ticket")
            print("2. Pay for Parking")
            print("3. Leave Garage")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.TakeTicket()
            elif choice == 2:
                self.Pay_for_Parking()
            elif choice == 3:
                self.leave_garage()
            else:
                print("Invalid choice")
                break
    


ParkingG= Parking_Garage(list(range(1,20)), list(range(1,20)), {"paid": False})
ParkingG.main()
ParkingG.EnterGarage()
ParkingG.TakeTicket()
ParkingG.Pay_for_Parking()
ParkingG.leave_garage()










