#The main agenda of inheritance is to reuse the code
#Single Inheritance- Parent to Child
class whatsappv1:
    def message(self):
        print("You can send message")
class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24 hrs")
monika=whatsappv1()
monika.message()
sai=whatsappv2()
sai.message()
sai.status() 

#Multilevel Inheritance-Parent to child and child to grand child
class whatsappv1:
    def message(self):
        print("You can send message")
class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24 hrs")
class whatsappv3(whatsappv2):
    def groups(self):
        print("You can create group and talk with many people at the same time")
monika=whatsappv1()
monika.message()
sai=whatsappv2()
sai.message()
sai.status() 
priyanka=whatsappv3()
priyanka.message()
priyanka.status()
priyanka.groups()

#Multiple Inheritance-Single child to multiple parents
#It is also a hybrid inheritance because it contains multiple and multilevel inheritance
class whatsappv1:
    def message(self):
        print("You can send message")
class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24 hrs")
class whatsappv3:
    def groups(self):
        print("You can create group and talk with many people at the same time")
class whatsappv4:
    def community(self):
        print("You can combine multiple groups")
class whatsappv5(whatsappv2,whatsappv3,whatsappv4):
    def channels(self):
        print("You can post regularly with huge number of people") 
priyanka=whatsappv5()
priyanka.groups()
priyanka.message()
priyanka.status()
priyanka.community()
priyanka.channels()

#Hierarchial Inheritance-Single Parent and Multiple Childs 
class whatsappv1:
    def message(self):
        print("You can send message")
class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24 hrs")
class whatsappv3(whatsappv1):
    def groups(self):
        print("You can create group and talk with many people at the same time")
class whatsappv4(whatsappv1):
    def community(self):
        print("You can combine multiple groups")
class whatsappv5(whatsappv1):
    def channels(self):
        print("You can post regularly with huge number of people") 
monika=whatsappv1()
monika.message()
sai=whatsappv2()
sai.message()
sai.status()
priyanka=whatsappv3()
priyanka.message()
priyanka.groups()
prasanna=whatsappv4()
prasanna.message()
prasanna.community()
gayathri=whatsappv5()
gayathri.message()
gayathri.channels()
