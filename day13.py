
#Exercise 1
def outer(hello):
    #text is having the scope of outer function
    string1 = hello
    def inner():
        #using non-local variable text
        print(string1)
    #return inner function
    return inner 
#if __name__=='__main__':
func = outer('Hello Sharath')
func()

#Exercise 2
def decorator(m):
    def operation(n):
        return m + n
    return operation
string1 = decorator("Hi")
string2 = decorator("Hello")
string3 = string1(" Buddy")
string4 = string2(" Buddy")
print(string3)
print(string4)

