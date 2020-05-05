#Exercise1
list1 = ["A","B","C","D"]
list2 = ["E","F","G","H"]
n=len(list1)
result = []
for i in range(0,n,1):
    s=list1[i]+list2[i]
    result.append(s)
print(result)


#Exercise2
x=""
for i in range (1,6):
    x=x+str(i)
    print(x)

#Exercise3
string=input("Enter string: ")
count1=0
count2=0
count3=0
count4=0
for i in string:
      if(i.islower()):
          count1=count1+1     
      elif(i.isupper()):
          count2=count2+1     
      elif(i.isdigit()):
          count3=count3+1
      else: count4=count4+1
print("The number of lowercase characters is: {}".format(count1))
print("The number of uppercase characters is:{}".format(count2)) 
print("The number of digits is:{}".format(count3)) 
print("The number of special characters is:{}".format(count4))