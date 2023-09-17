dictionary= {
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Cho": "Raven Claw",
    "Draco": "Slitherin",
    "Luna": "Raven Claw"
}
dictionary["Hermione"] ="Gryffindor"

#print(dictionary)

def square(n):
    return n*n

class Book():
    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1= Book("Harry Potter", "JK Rowling", 450)

#print(book1.author, book1.title, book1.pages)


#A program of adding passengers to the train if the capacity is not yet full
class Train():
    def __init__(self, capacity):
        self.capacity = capacity
        self.travellers = []

    def addTraveller(self, name):
        if not self.available():
            return False
        self.travellers.append(name)
        return True

    def available(self):
        return self.capacity- len(self.travellers)

hogwarts = Train(4)
people= ["Harry","Ron","Hermione","Ginny", "Draco","Luna","Nethal"]
'''for person in people:
    success= hogwarts.addTraveller(person)
    if success:
        print(f"We have successfully added {person} to the train")
    else:
        print(f"We have failed to add {person} to the train")
'''

#implementing a function that will sort names alphabetically in a list of dictionaries\

students= [
    {'name': 'Harry', "House": "Gryffindor"},
    {'name': 'Draco', "House": "Slitherin"},
    {'name': 'Cho', "House":"Ravenclaw"}
]

students.sort(key=lambda person: person["House"])

#print(students)


#writing a program that will try to catch exceptions or errors, in this case, a valueError and a zeroDivisionError
import sys
try:
    x= int(input("Enter a number: "))
    y= int(input("Enter another number: "))



except ValueError:
    print("Invalid input")
    sys.exit(1)

try:
    result = x/y
    print(result)
except ZeroDivisionError:
    print("OOPS! You can't divide by zero") 
