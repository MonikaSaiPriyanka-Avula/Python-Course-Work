#super()-Whenever we have same method in both the parent class and child class if we want to access the properties from parent class to child class we have to use super()
'''class whatsappv1:
    def status(self):
        print("You can upload status for 24 hrs")
class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can add music and you can react")
monika=whatsappv1()
monika.status()
priyanka=whatsappv2()
priyanka.status() '''

#When we have multiple inheritance we have to use class methods
class whatsappv1:
    def status(self):
        print("You can upload status for 24 hrs")
class whatsappv2:
    def status(self):
        print("You can add music and you can react")
class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can add to the cross platforms")
monika=whatsappv3()
monika.status()


