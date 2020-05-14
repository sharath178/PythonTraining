#Exercise 1
'''
#syntax error
print "hello world

#name error
def myfunction(a):    
    b = a - 2
    return b
c = 3
if c > 2:    
    d = my_function(5)
    print(d)

#Type Error
def my_function(a,e):    
    b = a - 2
    return b
c = 3
if c > 2:    
    d = my_function(5)
    print(d)

#Index Error
list1= [12,14,33,43,55,99]
print(list1[6])

#Key Error
my_dict = {'a':'1','b':'2'}
print(my_dict['c'])

#Attribute Error
integer =8
integer.append(9)
print(integer)

#Value Error
x = int("Hello")
'''

#Exercise 2
class HandlingException(Exception): pass

def getInput(user_input):

  input_list = user_input.split()
  if len(input_list) != 3:
    raise ExpressionError('Input does not consist of three elements') #Name error
  n1, op, n2 = input_list
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
    raise ExpressionError('The first and third input value must be numbers') # Value Error
  return n1, op, n2


def calculate(n1, op, n2):

  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2
  raise ExpressionError('{0} is not a valid operator'.format(op)) #


while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  n1, op, n2 = getInput(user_input)
  result = calculate(n1, op, n2)
  print(result)