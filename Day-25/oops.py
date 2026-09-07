#Syntax of class
'''classkeyword classname:'''
class Flipkart:
    pass

#Creating an object
monika=Flipkart()
sai=Flipkart()
priyanka=Flipkart()

#Using Class and Instance Attributes
class Flipkart:
    discount=30
    def info(self,name,phoneno,address):
        self.name=name
        self.phoneno=phoneno
        self.address=address
        print(f'Welcome to the Flipkart',self.name)
monika=Flipkart()
monika.info('monika',987654321,'Hyd')
sai=Flipkart()
sai.info('sai',876543219,'Banglore')
priyanka=Flipkart()
priyanka.info('priyanka',765432189,'chennai')

#Using Class, Instance and Static Methods
class Flipkart:
    discount=30

    @classmethod
    def updatediscount(cls):
        cls.discount=40
        print("Updated Discount:",cls.discount)

    def info(self,name,phoneno,address):
        self.name=name
        self.phoneno=phoneno
        self.address=address
        print(f'Welcome to the Flipkart',self.name)

    @staticmethod
    def banner():
        print(f"{Flipkart.discount}% is going, grab the products....")

monika=Flipkart()
monika.info('monika',987654321,'Hyd')
monika.updatediscount()
monika.banner()

sai=Flipkart()
sai.info('sai',876543219,'Banglore')
sai.updatediscount()
sai.banner()

priyanka=Flipkart()
priyanka.info('priyanka',765432189,'chennai')
priyanka.updatediscount()
priyanka.banner() 