#Practical 24
# Inheritance: Write a Program to: To create Class Person with attributes First name and Last name inherited by Subclass Student
# to print Name of Student using PrintMethod( )

class Person :
     def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Student(Person):
     def __init__(self, fname, lname):
       super().__init__(fname, lname)

     def PrintMethod(self):
           print("hello ," ,self.firstname, self.lastname)

obj = Student("john" , "Doe")           
obj.PrintMethod()