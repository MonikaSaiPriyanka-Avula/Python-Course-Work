class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._post=[]
    def getpassword(self):   #This method is defined to access private variable outside the function
        return self.__password
    @property    #For accessing protected variable outside the function the property is created
    def accesspost(self):
        return self._post
monika=Instagram("monika","1234567")
print(monika.username)
print(monika.getpassword()) 
print(monika.accesspost)

#For updating the public,private and protected variables
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._post=[]
    def getpassword(self):   
        return self.__password
    def setpassword(self,newpassword):   #This method is used to update the password in the private variable
        self.__password=newpassword
    @property    
    def accesspost(self):
        return self._post
    @accesspost.setter               #This is used to update the protected variable  
    def accesspost(self,newpost):
        self._post.append(newpost)
monika=Instagram("monika","1234567")
monika.username="monika_345"
print(monika.username) 
monika.setpassword("monika@123")
print(monika.getpassword())
monika.accesspost="Intro"
monika.accesspost="OOPS"
monika.accesspost="Project"
print(monika.accesspost)