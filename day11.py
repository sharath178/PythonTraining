#Exercise 1

def generate(n):
    for i in range(n,0,-1):
        yield i
num = int(input('Enter number '))
for item in generate(num):
    print(item)

#Exercise 2
import logging
def my_decorator(func):
  def inner1(*args):
    print("Start of inner method")
    response = func(*args)
    print(response)
    print("End of inner method")
    return response
  return inner1

logging.basicConfig(filename="logfile.log",filemode='w')
logger=logging.getLogger()

logger.setLevel(logging.INFO)
@my_decorator
def sum(num1, num2):
  return num1 + num2
a = 5
b = 7
#c = my_decorator(sum)
#result = c(a,b)
result = sum(a,b)
logger.info('Sum of the numbers is %d',result)