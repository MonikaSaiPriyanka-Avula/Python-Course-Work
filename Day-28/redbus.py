from abc import ABC, abstractmethod
class Redbus:
    bus={i: "Available" for i in range(1,11)}
    
    def displayseats(self):
        print("--------XYZ Bus---------")
        for i in Redbus.bus:
            print(i,Redbus.bus[i])
    def booking(self,seatno):
        for i in Redbus.bus:
            if i==seatno and Redbus.bus[i]=="Available":
                Redbus.bus[i]="Booked"
                print(f"Your seat-{seatno} is succesfully booked")
                break
        else:
            print(f"Your seat-{seatno} has already booked")

class Users(Redbus):
    def __init__(self,name,email,phoneno):
        self.name=name
        self.email=email
        self.phoneno=phoneno
        print(f"Hello {self.name},Welcome to RedBus")
class Driver:

    def __init__(self,name,experience,bus_no,phno):
        self.__name = name
        self.__experience = experience
        self.__bus_no = bus_no
        self.__phno=phno
    def display_driver_name(self):
        print("Driver Name:", self.__name)
    def display_driver_phno(self):
        print("Driver phno:", self.__phno)
class Payment(ABC):
    def source(self):
        print("Scanner / UPI ID / Mobile Number")
    def amount(self):
        print("Enter an amount")
    def bank(self):
        print("Choose your bank")
    def pin(self):
        print("Enter a PIN")
    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment Status: Success")
class HDFC(Payment):
    def paymentprocess(self):
        print("Payment is processed through HDFC")

class ICIC(Payment):
    def paymentprocess(self):
        print("Payment is processed through ICICI")

class Union(Payment):
    def paymentprocess(self):
        print("Payment is processed through Union Bank")

class Axis(Payment):
    def paymentprocess(self):
        print("Payment is processed through Axis Bank")

monika = Users("monika", 9876543210, "monika@gmail.com")
monika.displayseats()
monika.booking(4)
print("\nSeats after booking:")
monika.displayseats()
print("\n------------- DRIVER DETAILS -------------")
d = Driver(
    "ABC",
    "9876543210"
)
d.display_driver_name()
d.display_driver_phno()
print("\n------------- PAYMENT -------------")
payment = HDFC()
payment.source()
payment.amount()
payment.bank()
payment.pin()
payment.paymentprocess()
payment.paymentstatus()
