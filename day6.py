#Exercise 1
sampleList = [1,4,1,5,4,4,9,9]
sampleList = list(dict.fromkeys(sampleList))
print(sampleList)
maxNum = max(sampleList)
minNum = min(sampleList)
sampleTuple = (minNum,maxNum)
print(sampleTuple)

#Exercise 2
def bubbleSort(nlist):
    for j in range(len(nlist)-1,0,-1):
        for i in range(j):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
nlist = [13,4,34,23,14,55,67,99,87]
bubbleSort(nlist)
print(nlist)

#Exercise 3
import queue #module
q = queue.Queue() #class
for x in range(5):
    q.put(str(x))
while not q.empty():
    print(q.get(), end=" ")
print()

import queue #module
q = queue.LifoQueue() #class
for x in range(5):
    q.put(str(x))
while not q.empty():
    print(q.get(), end=" ")
print()



