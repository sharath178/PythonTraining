#Exercise 1
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
ExpectedTuple = tuple(sorted(tuple1, key=lambda item: item[1]))
print(ExpectedTuple)

#Exercise 2
setA = (1, 2, 3, 4)
setB = (5, 6, 7, 8)

setC = setA + setB
setD = sorted(setC)

print(setC)
print(setD)
print(setD[3])
print(setD[-3:])
print(len(setD))

#Exercise 3
import numpy as np 
x=np.array(dir(np))
total=len(x)
sort_list = sorted(x)
matching = [s for s in sort_list if "find" in s]
print(matching)
