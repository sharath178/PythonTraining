
#Exercise 1
import re
def check(string):
    result = re.compile(r'[a-zA-Z0-9.]') # use not
    string1 = result.search(string)
    print(string1)
    return bool(string1)     #use not to negate
word = input("Enter a string: ")
print(check(word))


#Exercise 2
import re
SampleData = ["XYZ(.com))))", "ABC", "jk(l(.com)", "po(l(.com)"]
for data in SampleData:
    print(re.sub(r" ?\([^()]+\)", "", data))

#Exercise 3
import re 
regex = '[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email):
    if(re.search(regex,email)):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email")  
email = input("Email: ")
check(email)
