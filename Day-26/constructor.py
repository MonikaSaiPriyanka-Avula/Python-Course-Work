#A constructor is a special method that is called automatically whenever an object is created
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        print(f"Welocome to Instagram,{self.username}")
monika=Instagram("monika","1234567")
sai=Instagram("sai","67890")
priyanka=Instagram("priyanka","45678") 