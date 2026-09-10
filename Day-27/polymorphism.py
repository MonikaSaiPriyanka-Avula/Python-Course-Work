#Method Overloading-Same method but different parameters but python doesn't support it if we have to use we need default arguments
#Method Overriding-Same method and same parameters but one in parent class and other in child class
class Hotstar:
    def __init__(self,name):
        print(f"-----Welcome to Hotstar,{name}-----")
    def auth(self):
        print("You can Login/Register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can Search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("play pause resume")
    def ads(self):
        print("The ads will run")
    def quality(self):
        print("You have limited quality")
    def devices(self):
        print("You have only a single login")
    def access(self):
        print("You have limited access")
    def download(self):
        print("You can't download")

class PremiumHotstar:
    def __init__(self,name):
        print(f"-----Welcome to Premium Hotstar,{name}-----")
    def auth(self):
        print("You can Login/Register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can Search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("play pause resume")
    def ads(self):
        print("The ads will not run")
    def quality(self):
        print("You have High quality")
    def devices(self):
        print("You have multiple login")
    def access(self):
        print("You have Unlimited access")
    def download(self):
        print("You can download")
monika=Hotstar("monika")
monika.auth()
monika.dashboard()
monika.search()
monika.history()
monika.playcontrollers()
monika.ads()
monika.quality()
monika.devices()
monika.access()
monika.download()

Priyanka=PremiumHotstar("priyanka")
Priyanka.auth()
Priyanka.dashboard()
Priyanka.search()
Priyanka.history()
Priyanka.playcontrollers()
Priyanka.ads()
Priyanka.quality()
Priyanka.devices()
Priyanka.access()
Priyanka.download()