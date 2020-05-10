#Exercise 1
class Cars:
  def __init__(car, name, model, worth):
    car.name = name
    car.model = model
    car.worth = worth

  def myfunc(car):
    print("Car name is: "+car.name)
    print("Car model is: "+car.model)
    print("Car worth is: "+car.worth)

carA = Cars("Ford", "Black Sedan","$50000")
carA.myfunc()
carB = Cars("Jeep", "Red Truck","$10000")
carB.myfunc()

#Exercise 2
class StringReversal:
    def init(self, s):
        return ' '.join(reversed(s.split()))
string = input("Enter String ")
print(StringReversal().init(string))

#Exercise 3
setA = {1,2,3,4}
setB = {1,3,5,7}
setC = setA | setB
setD = setA - setB
setE = setB - setA
setF = setA & setB
setG = setA ^ setB
print(setA)
print(setB)
print(setC)
print(setD)
print(setE)
print(setF)
print(setG)
print(len(setC))

#Exercise 4
directory = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
}

directory["Jane Doe"] = "+27 555 1024"
directory["Anna Cooper"] = "+27 555 3237"

print(directory["Bob Stone"])
print(directory.get("Bob Stone", None))

print(directory.keys())
print(directory.values())

