#Defining book class
class book:
    def __init__(self,title="The Only Pirate at the Party",author="Lindsey Stirling",publisher="Gallery Books",price=708,quantity=1000):
        #Defining variables
        self._title=title
        self._author=author
        self._publisher=publisher
        self._price=price
        self._quantity=quantity
        self.tot_royality=0
    #Getter and Setter Method for each instance variables in the class
    def get_title(self):
        return self._title
    def set_title(self,title):
        self._title=title
        return
    def get_author(self):
        return self._author
    def set_author(self,author):
        self._author=author
        return
    def get_publisher(self):
        return self._publisher
    def set_publisher(self,publisher):
        self._publisher=publisher
        return
    def get_price(self):
        return self._price
    def set_price(self,price):
        self._price=price
        return
    #Getter and Setter Method for Quantitiy Sold
    def get_quantity(self):
        return self._quantity
    def set_quantity(self,quantity):
        self._quantity=quantity
        return
    #Royality Calcularion
    def royality(self):
        if self._quantity<=500 and self._quantity>0:
            self.tot_royality+=self._quantity*self._price*(10/100)
        elif (self._quantity-500)>0 and (self._quantity-500)<=1000:
            self.tot_royality+=(self._quantity-500)*self._price*(12.5/100)+500*self._price*(10/100)
        elif (self._quantity-1500)>0:
            self.tot_royality+=(self._quantity-1500)*self._price*(15/100)+500*self._price*(12.5/100)+500*self._price*(10/100)
        return self.tot_royality
#Creating a Inherited Class ebook
class ebook(book):
    def __init(self,format_type="pdf"):
        self._format=format_type
    #Defining a Getter and Setter Method for format type
    def get_format(self):
        return self._format
    def set_format(self,format_type):
        self._format=format_type
        return
    def royality(self):
        if self._quantity<=500 and self._quantity>0:
            self.tot_royality+=self._quantity*self._price*(10/100)
        elif (self._quantity-500)>0 and (self._quantity-500)<=1000:
            self.tot_royality+=(self._quantity-500)*self._price*(12.5/100)+500*self._price*(10/100)
        elif (self._quantity-1500)>0:
            self.tot_royality+=(self._quantity-1500)*self._price*(15/100)+1000*self._price*(12.5/100)+500*self._price*(10/100)
        self.tot_royality-=((12/100)*self.tot_royality)
        return self.tot_royality
#Collecting the date from the user
title=input("Enter the Title of the Book: ")
author=input("Enter the Name of the Author: ")
publisher=input("Enter the Name of Publisher: ")
price=int(input("Enter the Price of the Book: "))
quantity=int(input("Enter the Number of Books Sold: "))
#Creating objects from the new classes and assigning the input data
bk=book()
bk.set_title(title)
bk.set_author(author)
bk.set_publisher(publisher)
bk.set_price(price)
bk.set_quantity(quantity)
bkty=ebook()
bkty.set_title(title)
bkty.set_author(author)
bkty.set_publisher(publisher)
bkty.set_price(price)
bkty.set_quantity(quantity)
#Checking if the book is a ebook or not and giving the required output
bk_type=int(input("Enter 1 if its a physical book and 2 if it is an ebook: "))
print()
if bk_type==1:
    print("Title: ",bk._title)
    print("Author: ",bk._author)
    print("Publisher: ",bk._publisher)
    print("Format: Book")
    print("Quantity Sold: ",bk._quantity)
    roy=bk.royality()
    print("Royality: ",roy)
if bk_type==2:
    ebookty=str(input("Enter the Ebook format: "))
    bkty.set_format(ebookty)
    print("Title: ",bkty._title)
    print("Author: ",bkty._author)
    print("Publisher: ",bkty._publisher)
    print("Format: EBook")
    print("Quantity Sold: ",bkty._quantity)
    roy=bkty.royality()
    print("Royality: ",roy)
