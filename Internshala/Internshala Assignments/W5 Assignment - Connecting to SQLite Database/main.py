#Importing the SQLite modult
import sqlite3
#Establishing a connection
shelf=sqlite3.connect("bookshelf.db")
curshelf=shelf.cursor()
#Creating Necessary Variables
total_cost=0
#Accepting User Input Values
while True:
    title=str(input("Title: "))
    curshelf.execute("SELECT * FROM shelf WHERE title='"+title+"';")
    record=curshelf.fetchone()
    print(record)
    quantity=int(input("Quantity: "))
    total_cost+=record[3]*quantity
    moreb=str(input("Add more Books:? Y/N: "))
    if moreb=="N" or moreb=="n":
        break;
print("Total Cost is: ",total_cost)
#Closing the connection
shelf.close()
