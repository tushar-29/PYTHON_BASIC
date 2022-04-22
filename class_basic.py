class Dog:
    # class variable access to class, all other objects
    animal = "dog"

    def __init__(self, breed, color):
        self.__color = color
        self.breed = breed

    def get_color(self):
        return self.__color


dog_1 = Dog("pug", "white")
print("dog_1 is ", dog_1.animal)
print("dog_1 breed is ", dog_1.breed)
# print("dog_1 color is ", dog_1.__color)   # private group
print("dog_1 color is ", dog_1.get_color())

dog_2 = Dog("bulldog", "gray")
print("dog_2 is ", dog_2.animal)
print("dog_2 breed is ", dog_2.breed)
print("dog_2 color is ", dog_2.get_color())

dog_2.animal = "cat"
print("dog_1 is ", dog_1.animal)
print("dog_2 is ", dog_2.animal)
Dog.animal = "wolf"
print("dog_1 is ", dog_1.animal)
print("dog_2 is ", dog_2.animal)
print("\n\n")



class Student:
    Class = 10
    year = 2021

    def __init__(self):
        self.name = None
        self.roll = None
        self.sec = None

    def student_entry(self):
        #     self.name = input("Enter your name ? : ").strip()
        #     self.roll = int(input("Enter your roll no. : "))
        #     self.sec = input("Enter Section : ")[0].upper()
        self.name = "Tushar Prasad"
        self.roll = 1
        self.sec = 'D'

    def display(self):
        print(f"Name : {self.name}\nRoll no. : {self.roll}\nSection : {self.sec}")

    def __del__(self):
        print("Memory is been free")


student_list = []
flag = 1
count = 0
while flag and count < 2:
    obj = Student()
    obj.student_entry()
    student_list.append(obj)
    count += 1
    # flag = flag + 1 if input("Do you want to add more ?(Y/N) : ") == 'Y' else 0

for i in range(count):
    student_list[i].display()

del student_list


# inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):
    def is_employee(self):
        return True


s1 = Person("Roy")
s2 = Employee("James")
print(f"{s1.get_name()} is a person and employee status is {s1.is_employee()}")
print(f"{s2.get_name()} is a employee and status is {s2.is_employee()}")


# cunstructor inheritance

class Person2:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.emp = False

    def get_info(self):
        return f"{self.name} and age is {self.age}"

    def is_employee(self):
        return self.emp


class Employee2(Person2):

    def __init__(self, name, age, dept, course):
        self.dept = dept
        self.course = course
        Person2.__init__(self, name, age)  # without this we cant store name as emp obj to person

    def get_info(self):
        return f"\ndepartment is {self.dept} and course is {self.course}"


p1 = Employee2("Roy", 19, 'CSE', "B.tech")
print(p1.get_info())


# single inheritance and multi - inheritance


class A:
    def __init__(self, name):
        self.name = name
        self.__private = True
        self._protected = False


class B:
    def __init__(self, age):
        self.age = age



class C(A, B):
    def __init__(self, name, age, address):
        self.address = address
        A.__init__(self, name)
        B.__init__(self, age)

    def get_private(self):
        print(self.__private)

    # can be accessed
    def get_protected(self):
        print(self._protected)

obj_1 = C(name="Roy", age=18, address="India")
print(obj_1.name, obj_1.age, obj_1.address)
# obj_1.get_private() # error
obj_1.get_protected()
print(obj_1._protected)
obj_1._protected = True
print(obj_1._protected)



# print(obj_1.__private) # private veriable can't be acced from inheritanc

# multi level


class D(C):
    def __init__(self, name, age, address, emp):
        self.emp = emp
        C.__init__(self, name, age, address)


obj_2 = D(name="Root", address="USA", age=21, emp=False)
print(obj_2.name, obj_2.age, obj_2.address, obj_2.emp)


# Polymorphism

class India:
    type = "Country"
    def intro(self):
        print("India is land of all seasons")

    def is_develop(self):
        print("It is developing country")

class Sikkim(India):
    type = "Indian State"
    # intro change for sikkim
    def intro(self):
        print("Sikkim is where nature smile")


def funct(o1):
    o1.intro()
    o1.is_develop()

ind = India()
sk = Sikkim()

funct(ind)
funct(sk)

# class store variable as class variable or instance variable
#eg: CSE student have CSE as class variable and name, roll_no as
# instance Variabel

class BTech:
    department = "CSE"  # class variable
    def __init__(self):
        self.name = "Tushar" #instance variable

obj_5 = BTech()
obj_6 = BTech()
print(obj_5.department)
print(obj_6.department)
obj_5.department = "EEE"
BTech.department = "IT"
# Since obj change class variable so that obj have unique class variable
print(obj_5.department)
print(BTech.department)
# obj class variable Changes With change of Class variable using class name
# obj_6 has not change class variable by itself class variable is changed
#due to change done by class name to class variable
print(obj_6.department)
print("\n\n")



# static method and class method

# A class method takes cls as first parameter
# while a static method needs no specific parameters.

# A class method can access or modify class state
# while a static method can’t access or modify it.

# In general, static methods know nothing about class state.
# They are utility type methods that take some parameters and
# work upon those parameters.
# On the other hand class methods must have class as parameter

from datetime import date

class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def age_by_dob(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return (True if age >=18 else False)

obj_7 = Person3("Sky", 21)
print(obj_7.is_adult(obj_7.age))
obj_8 = Person3.age_by_dob("Brut", 2002)
print(obj_8.age)


# use of super()

class Animal:
    def __init__(self, name, is_worm):
        self.name = name
        self.is_worm = is_worm

    def is_domestic(self):
        return True

class Dog(Animal):
    def __init__(self, typ, name, is_worm):
        self.typ = typ
        super().__init__(name, is_worm)

    def is_domestic(self):
        result = super().is_domestic()
        return result+1

p = Dog('pug', 'Dog', True)
print(p.name, p.typ, p.is_worm)
print(p.is_domestic())

#%%
