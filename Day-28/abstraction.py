#Abtsraction is used when we have to restrict something in the parent class and there we should not create an object in the parent class
#When we restricted something we have to use the same method when we have even n number of child classes
#ABS stands for abstract base class
from abc import ABC,abstractmethod
class Payment(ABC):
    def source(self):
        print("Scanner/UPI Id/Mobile Number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("Select the bank") 
    def pin(self):
        print("Enter the pin")
    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment Success/Fail") 
class HDFC(Payment):
    def paymentprocess(self):
        print("Payment Process through HDFC Bank") 
class ICIC(Payment):
    def paymentprocess(self):
        print("Payment process through ICIC Bank")
class UNION(Payment):
    def paymentprocess(self):
        print("Payment process through UNION Bank")
class AXIS(Payment):
    def paymentprocess(self):
        print("Payment process through AXIS Bank")
monika=HDFC()
monika.source()
monika.amount()
monika.bank()
monika.pin()
monika.paymentprocess()
monika.paymentstatus()

sai=ICIC()
sai.source()
sai.amount()
sai.bank()
sai.pin()
sai.paymentprocess()
sai.paymentstatus()

priyanka=UNION()
priyanka.source()
priyanka.amount()
priyanka.bank()
priyanka.pin()
priyanka.paymentprocess()
priyanka.paymentstatus()

prasanna=AXIS()
prasanna.source()
prasanna.amount()
prasanna.bank()
prasanna.pin()
prasanna.paymentprocess()
prasanna.paymentstatus()
