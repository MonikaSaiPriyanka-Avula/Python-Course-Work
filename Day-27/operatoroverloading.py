#Operator Overloading-It is used to overload the operators to overload with objects and they are used by using magic methods
class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __truediv__(self,other):
        return self.n/other.n
    def __floordiv__(self,other):
        return self.n//other.n
    def __mod__(self,other):
        return self.n%other.n
    def __pow__(self,other):
        return self.n**other.n
    def __gt__(self,other):
        return self.n>other.n
    def __lt__(self,other):
        return self.n<other.n 
    def __ge__(self,other):
        return self.n>=other.n
    def __le__(self,other):
        return self.n<=other.n
    def __eq__(self,other):
        return self.n==other.n
    def __ne__(self,other):
        return self.n!=other.n
    def __str__(self):  #It is used to get the values what we have given and they are converted into strings
        return str(self.n)
    
a=Number(5)
b=Number(25)
print(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)
