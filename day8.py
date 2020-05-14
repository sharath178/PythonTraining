#Exercise 1
import csv
output_rows = []
with open('csv_file1.csv','r') as file:
    reader = csv.reader(file)
    for line in reader:
        line[1], line[2] = line[2], line[1]
        row = [int(i) for i in line]
        row.append(sum(row))
        output_rows.append(row)
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output_rows)
f= open("out.csv","r")
print(f.read())

#Exercise 2
import json
print(json.dumps({"name": "Sharath", "age": 24}))
print(json.dumps(["Hi", "Hello"]))
print(json.dumps("hello"))
print(json.dumps(108))
print(json.dumps(19.19))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Exercise 3
import csv
csv_columns = ['Jane Doe','John Smith','Bob Stone']
directory = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
}
csv_file = 'Directory.csv'
try:
   with open(csv_file, 'w') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
       writer.writeheader()
       for data in directory:
           writer.writerow(directory)
except IOError:
   print("I/O error")
data = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
#for row in data:
   #print(row)
f = open("Directory.csv", "r")
print(f.read())