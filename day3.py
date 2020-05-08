#Exercise 1
def recursion(k):
  if(k < 2):
    return 0
  return k + recursion(k-1)
print(recursion(20))

#Exercise 2
list1= [12,14,33,43,55,75.99,132,150,180,199]
l=[]
for x in list1:
    if (x>=150):
        break
    elif x % 3 == 0:
      l.append(x)
      
print("Numbers divisible by 3 are:",l)

#Exercise 3
def my_function(a):    
    b = a - 2
    return b
c = 3
if c > 2:    
    d = my_function(5)
    print(d)
#  a and b inside function. c and d throughout program
#  a and b inside function. c when declared and d inside if block. Both terminate at the end of program
#  d doesn't get printed and function isn't called
#  Declare d outside loop and initialise it

