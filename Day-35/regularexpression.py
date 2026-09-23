#Match is used to find whether the text is present in the pattern or not only starting
'''import re
pattern=r'[0-9]'
text="Codegnan2026"
res=re.match(pattern,text)
print(res.group() if res else "Pattern not matched")

#Search is used to check the pattern in the entire description
import re
pattern=r'[0-9]'
text="Codegnan2026"
res=re.search(pattern,text)
print(res.group() if res else "Pattern not matched")

#Findall gives the result in a list when it finds the pattern in the text
import re
pattern=r'[0-9]'
text="Codegnan2026"
res=re.findall(pattern,text)
print(res)

#Finditer gives the result of indexes and the patterns where it is started and we have to iterate it because it is a lazy loader
import re
pattern=r'[0-9]'
text="Codegnan2026"
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())

#Fullmatch is used to check the exact pattern and is used for validation
import re
pattern=r'[0-9]{10}'
text="Codegnan2026"
res=re.fullmatch(pattern,text)
print(res.group() if res else "Pattern not matched")

#Split is used to split even when we have more things to be seperated
import re
pattern=r'[,@:;_&]'
text='java,python@c:flask_mysql&django'
res=re.split(pattern,text)

#Sub-It is going to replace one pattern with other
import re
pattern=r'[aeiou0-9]'
text="python 30 mysql 23 flask 20 django 80"
res=re.sub(pattern,"*",text)
print(res)

#. is used to place anything in the text
import re
pattern=r'h.t'
text="hand loom hot hit hat hood wood"
res=re.findall(pattern,text)
print(res)

#^ is used for startswith
import re
pattern=r'^[a-z]'
text="hand loom hot hit hat hood wood"
res=re.findall(pattern,text)
print(res)

#$ is used for endswith
import re
pattern=r'[a-z]$'
text="hand loom hot hit hat hood wood"
res=re.findall(pattern,text)
print(res)

#* is used for 0 or 1 occurence
import re
pattern=r'ab*'
text="a ab abbbb abbbbbbbbbb aaabbbbbb"
res=re.findall(pattern,text)
print(res)

#+ is used to have atleast 1 or more occurence
import re
pattern=r'ab+'
text="a ab abbbb abbbbbbbbbb aaabbbbbb"
res=re.findall(pattern,text)
print(res)

# | is used for any one of the thing
import re
pattern=r'(91|0)'
text="0987651234"
res=re.findall(pattern,text)
print(res)

#[] is used to match any one character from the characters specified inside the brackets.
import re
pattern=r'[A-Za-z0-9]'
text="ASDFG098765xcvbn"
res=re.findall(pattern,text)
print(res)

# () is used to group characters/patterns together
import re
pattern=r'(aeiou)'
text="ASDFG098765xcvbn"
res=re.findall(pattern,text)
print(res)

#{} is used for the length
import re
pattern=r'[0-9]{2}'
text="ASDFG098765xcvbn"
res=re.findall(pattern,text)
print(res)

#w is used for letters, digits, _
import re
pattern=r'\w'
text="ASDFG098765xcvbn"
res=re.findall(pattern,text)
print(res)

#W is used for Not a word character like @,$,&
import re
pattern=r'\W'
text="ASDFG098765xcvbn"
res=re.findall(pattern,text)
print(res)

#s is used for Whitespace
import re
pattern=r'\s'
text="ASDFG098765xcvbn"
res=re.findall(pattern,text)
print(res)

#S is used for not whitespace
import re
pattern=r'\S'
text="ASDFG098765xcvbn"
res=re.findall(pattern,text)
print(res)

#d is used for Digit
import re
pattern=r'\d'
text="ASDFG098765xcvbn"
res=re.findall(pattern,text)
print(res)

#D is used for not digits
import re
pattern=r'\D'
text="ASDFG098765xcvbn"
res=re.findall(pattern,text)
print(res)

#Validating Name
import re
name=input("Enter the name:")
pattern=r'^[a-zA-Z]{2,25}( [a-zA-Z]{2,25})+$'
res=re.fullmatch(pattern,name)
print("Valid Name" if res else "Invalid Name")

#Validating Email
import re
email=input("Enter the Email:")
pattern=r'^[a-zA-Z._0-9]+@[a-zA-Z._0-9]+\.[A-Za-z]{2,}$'
res=re.fullmatch(pattern,email)
print("Valid Email" if res else "Invalid Email")

#Validating Phone Number
import re
phoneno=input("Enter the phoneno:")
pattern=r'^[6-9]\d{9}'
res=re.fullmatch(pattern,phoneno)
print("Valid Phoneno" if res else "Invalid Phoneno")'''

#Validating Pancard
import re
pancard=input("Enter the pancard:")
pattern=r'^[A-Z]{6}\d{4}[A-Z]{1}$'
res=re.fullmatch(pattern,pancard)
print("Valid pancard" if res else "Invalid pancard")









