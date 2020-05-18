
#Exercise 1 
import sqlite3
try:
   Connection = sqlite3.connect('temp.db')
   con = Connection.cursor()
   print("\nDatabase created and connected to SQLite.")
   sqlite_select_Query = "select sqlite_version()"
   con.execute(sqlite_select_Query)
   version = con.fetchall()
   print("\nSQLite Database Version is: ", version)
   con.close()
except mysql.Error as error:
   print("\nError while connecting to sqlite", error)
finally:
   if (Connection):
       Connection.close()
       print("\nThe SQLite connection is closed.")

#Exercise 2
import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
   try:
     conn = sqlite3.connect('mydb.db')
     return conn
   except Error:
     print(Error)
 
def sql_table(conn):
   cursorObj = conn.cursor()
   cursorObj.execute("CREATE TABLE Deloitte(EmpID n(5), name char(30))")
   cursorObj.executescript("""
   INSERT INTO Deloitte VALUES(555522,'Sharath');
   INSERT INTO Deloitte VALUES(543789,'Saurabh');
   INSERT INTO Deloitte VALUES(123456,'Anand');
   """)
   conn.commit()
   cursorObj.execute("SELECT * FROM Deloitte")
   rows = cursorObj.fetchall()
   print("Practitioner details:")
   for row in rows:
       print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")

#Exercise 3
import  sqlite3
conn  =  sqlite3.connect ( 'mydb.db' )
cursor  =  conn.cursor ()
EmpID = input('Employee ID:')
name = input('Name:')
cursor.execute("""
INSERT INTO Deloitte(EmpID, name)
VALUES (?,?)
""", (EmpID, name))
conn.commit ()
print ( 'Data entered successfully.' )	
cursor.execute("SELECT * FROM Deloitte")
rows = cursor.fetchall()
print("Practitioner details:")
for row in rows:
   print(row)
conn.close ()
if (conn):
  conn.close()
  print("\nThe SQLite connection is closed.")
