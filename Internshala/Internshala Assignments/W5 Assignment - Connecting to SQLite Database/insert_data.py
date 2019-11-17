#Importing Necessary Modules
import sqlite3
#Establishing a Connection
shelf=sqlite3.connect("bookshelf.db")
curshelf=shelf.cursor()
#Creating a table with error check
try:
    curshelf.execute('''CREATE TABLE shelf(number INT PRIMARY KEY NOT NULL ,title TEXT NOT NULL, author TEXT STRING, price FLOAT NOT NULL);''')
    shelf.commit()
    print("Table Created SUCCESSFULLY!")
except:
    print("ERROR in Creating a New Table!")
    shelf.rollback()
cont="y"
#Accepting the variables from the USER
while cont=="y":
    number=input("Enter Book Index: ")
    title=str(input("Title: "))
    author=str(input("Author: "))
    price=int(input("Price: "))
#Inserting the values into the records
    try:
        curshelf.execute("INSERT INTO shelf(number,title,author,price) VALUES(?,?,?,?)",(number,title,author,price))
        shelf.commit()
        print("Record ADDED SUCCESSFULLY!")
    except:
        print("ERROR in INSERT query!")
        shelf.rollback()
    cont=input("Add More Records? Y/N: ")
    if cont=="n" or cont=="N":
        print("DATA Entry Complete")
        break;
#Closing the Connection
shelf.close()
