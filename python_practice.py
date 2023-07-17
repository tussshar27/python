a=10
b=20
e="Tushar"
f="77"
c=True
d=None
print(a+b)
print(a,b)

print(23, 45, sep="!!!",end="007\n")    #sep means (seperatd by) and sep, end should be declared in the end

print(type(c))
print(a+int(f))     #typecasting string to int

# string is like an array.
s="This is a string"
print(s[1:2])
print(s[1:4])
for ch1 in s:
    print(ch1)

print(len(s))
print(s.upper())    #strng is unchangeable i.e it creates copy of main string and perform operation on it.

print(s.replace("Th","Tushar"))
print(s.split(" "))     #created list
print(type(s.split(" ")))

s2="sbc pQR NmO"
print(s2.capitalize())  #makes first letter capital and else small.

print(s2.index("p"))
print(s2.title())   #makes initial of all as capital
print(s2.swapcase())    #it swaps lower to upper and vice-versa

# if - else block
a=10
b=20

if (a>b):
    print("a is greater than b")
elif(a<b):
    print("a is smaller than b")
else:
    print("a is equal to b")

for i in range(1,10,3):
    print(i)

for j in range(1,5):
    print(j)


# match case statement
m=100

match m:
    case 0:
        print("0")
    case 10:
        print("10")
    case _ if m!=20:
        print("not 20")
    case _:
        print("other")

# while loop
i=5
while(i<10):
    print(i)
    i=i+1

# list
# list - [] is used -  Ordered, CHANGEABLE, allow duplicates

l = [10, 20, "Tushar", 34]  #changeable
print(l[1])
print(l.remove(34))
print(l)
l.reverse()
print(l)
l.append(7)
print(l)
# l.sort()
# print(l)

l2 = l.copy()   #new list
print(l2)

for i in l:
    print(i)

# for in loop
if 20 in l:
    print(20," is present")
else:
    print("no present")

# string
s = "I am the man!"
print(len(s))

# TUPLE     #unchangeable
t = (20, 3, 57, 21, "Annam")
print(t)
print(type(t))

# since its tuple so we can convert that to list and make changes and again convert it to tuple
l1 = list(t)
print(l1)
l2 = l1.copy()
l1.append(17)
print(l1)
t = tuple(l1)
t2 = tuple(l2)
print(t)
print(t2)

t3 = t + t2
print(t3)       #merging of two tuples

l3 = l1 + l2    #merging of two list
print(l3)

# f-string
abc="Tushar"
pqr="Annam"

name = "First name:{} and Lastname:{}"
print(name.format(abc,pqr))


name = "First name:{1} and Lastname:{0}"
print(name.format(abc,pqr))

name = f"First name:{abc} and Lastname:{{pqr}}"
print(name)

num=69.23999999999
txt = f"Your number is: {num:.3f}"  #it roundof and converts to decimal
print(txt)


# function
n=10
def func1(n):
    '''Takes in nmber n, returns the square of n'''
    return n+10

print(func1(20))
print(func1.__doc__)    #it prints comment present inside function

def func1(n):
    print(n+10)

func1(20)

# SET
# set is used to remove duplicates
# it is unordered collection of data
st = {2,3,5,5,"Tushar",6}
print(st)
print(type(st))

st2 = {}    #empty set is considered as dictionary
print(type(st2))

st3 = set() #mention set keyword if its empty
print(type(st3))

s1 = {2,3,4,55,6,2}
s2 = {4,5,6,7,7,8}
print(s1)
print(s2)
# print(s1.union(s2))
# print(s1.intersection(s2))  #intersect
#
# s3 = s1.update(s2)
# print(s3)

print(s1.intersection_update(s2))
print("s1",s1)

print(s1.symmetric_difference(s2))

print(s1.isdisjoint(s2))

print(s1.issuperset(s2))

print(s1.issubset(s2))

s1.add("Tushar")
print(s1)

s1.remove(4)
print(s1)

s1.clear()  #to delete all elements
print(s1)

s1 = {2,3,5,7,8,4,5}

if 0 in s1:
    print("7 is present in s1")
elif 4 in s1:
    print("4 is present in s1")
else:
    print("not present")


# DICTIONARIES
# ORDERED, FAST

d = {'name':'tushar','age':25,'eligible':True}
print(d)
print(type(d))
print(d['name'])
print(d['age'])
print(d['eligible'])
print(d.keys())
print(d.values())
print(d.items())
for key1,value1 in d.items():
    print(f"THe value to key {key1} is {value1}")

for key in d.keys():
    print(key)

emp = {12: 45, 34: 34, 6: 78, 87: 98}
emp2 = {223: 56, 887: 23}

emp.update(emp2)
print(emp)
emp.update({777:4})
print(emp)
emp.pop(6)
print(emp)
emp.clear()
print(emp)
del emp

# for - else block
# else will run after completely running for
for i in range(1,5):
    print(i)
else:
    print("else block in for")

i=5
while(i<10):
    print(i)
    i=i+1
else:
    print("else block in while")

# excepton handling
# try - except

try:
    # a = int(input("Enter number:"))
    a = 10
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except Exception as e:
    print(e)
print("after try except block")

try:
    l = [1,2,3,4,5]
    i = 9
    print(l[i])
except Exception as e:
    print(e)


def func1():
    try:
        l = [1, 2, 3, 4, 5]
        i = 9
        print(l[i])
    except Exception as e:
        print(e)
    # print("after try-except")
    finally:
        print("finally block")

func1()

# ENUMERATE FUNCTION
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(type(y))
print(list(y))
print(type(list(y)))

import math

print(dir(math))

from math import sqrt,pi
# i = int(input("Enter number to find squar of it:"))
i=2
r = sqrt(i)
print(r)

from tushar import welcome, tush
welcome()
print(tush)

# local and global variable
# local variables are declared inside a function
# where as global variables are declared outside a function or can declared inside a function but using global keyword and can be accessed anywhere.

x = 10
def func1():
    global x
    x = 20
    m = 50
    print(x)

print("outside function:" , x)
func1()
print("inside function:" , x)   #x value got changed bc global keyword
print(m)        #error: since its local var can't be accessed outside.

# reading a file
f = open("myfile.txt","r")
print(f.read())
f.close()

# writing a file
# two types: overwrite (w) and append (a)

# write
f = open("myfile.txt","w")
f.write("HEllo Tushar!!!!")
f.close()

# append
f = open("myfile.txt","a")
f.write("\nThis is second line")
f.close()

# lambda function
# eg. Q. to find cube

# normal function
def func1(n):
    y = n*n*n
    return y
print(func1(10))

# lambda function
cube = lambda n: n*n*n
print(cube(n))

square = lambda s: s*s
print(square(5))

avg = lambda x,y,z: (x+y+z)/3
print("average is:", avg(10,20,30))

# Q. to find cube of each element of list
cube = lambda c: c*c*c
print(cube(9))

l = [2,3,4,5,6]
ls = []
for i in l:
    a = cube(i)
    print(a)
    ls.append(cube(i))    #also to store it in empty list

print(ls)

# map, filter and reduce  built-in functions
# list is passed with function
# they take function as an argument
# above code using map function
# in below code, cube function and list are passed as an arguments
l2 = list(map(cube, l))
print(l2)
l3 = list(map(square, l))
print(l3)
print(type(l3))

# FILTER
def func1(a):
    return a > 4

print(func1(5))

l4 = list(filter(func1,l))
print(l4)

# REDUCE
# first import reduce
# from functools import reduce


# is vs ==
# is compares memory location where as == compare values

a=10
b=10

print(a==b)
print(a is b)

c=20
d='20'

print(c==d)
print(c is d)

c = [1,4,23]
d = [1,4,23]

print(c is d)   #False
print(c == d)   #True

# class & object
# NOTE: we must take parametrs only from class, if we pass parameters from function then it will throw error.
# To avoid the error, we can use staticmethod concept as shown later below code
class Person:
    name = "Tushar Annam"   #class variable     #concept shown in later below code
    occupation = "DE"
    age = 25

    def func1(self):    #self is always declared as an argument in function
        print(f"Name: {self.name}, Occupation: {self.occupation}, Age: {self.age}")

p = Person()
print(p.name)
print(p.occupation)
print(p.age)
p.func1()

class Department:
    dept_id = 1
    dept_name = 'IT'
    dept_strength = 10000

    def info(self):
        print(f"Dept_id: {self.dept_id}, Dept_name: {self.dept_name}, Dept_strength: {self.dept_strength}")

d = Department()
print(d.dept_id)
print(d.dept_name)
print(d.dept_strength)
d.info()

e = Department()
e.dept_id=27
e.dept_name="HR"
e.dept_strength=100
print(e.dept_id)
print(e.dept_name)
print(e.dept_strength)
e.info()

# CONSTRUCTOR
# The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
# In Python the __init__() method is called the constructor and is always called when an object is created.
# the above code can written using constructor
# __init__(self) is a special method used to build constructor

class Cons:
    def __init__(self):
        print("This is called from initial constructor")

c = Cons()     # whenever object is created, constructor is called by default

class Para_cons:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o
        print(f"Called from object; Name: {self.name}, Occupation: {self.occupation}")

    def info(self):
        print(f"Name: {self.name}, Occupation: {self.occupation}")

pc = Para_cons("Tushar","IT")
# pc = Para_cons()    #error: missing two parameters
pc.info()

# DECORATOR
# a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.
# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.
# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function.

def greeting(func):     #hello function is passed as an argument
    def modfunc():      #new function is created.
        print("Good Morning")
        func()      #below hello function is called
        print("Bye, Good day to you!")
    return modfunc      #decorated function


@greeting
def hello():
    print("Hello World!")

hello()


# *args are the way to take all the arguments as tuples,
# **kwargs are  the way to take all the arguments as dictionaries

def greeting(func):     #hello function is passed as an argument
    def modfunc(*args, **kwargs):      #new function is created.
        print("Good Morning")
        func(*args, **kwargs)      #below hello function is called
        print("Bye, Good day to you!")
    return modfunc      #decorated function

@greeting
def add(a,b,c,d):
    print("Add:",a+b+c+d)

# @greeting     #error: bc below its called in alternate way
def sub(a,b,c,d):
    print("Subtract:",a-b-c-d)

add(10,20,30,40)    #function is called

greeting(sub)(10,20,30,40)  #alternate way to call decorator function


# GETTER
# in getter, we can call a function as a variable attribute
# eg. instead of calling object.function(), we can call as object.function
# we have to define @property decorator above function creation to use as a getter function

class MyClass:
    def __init__(self, value):
        self._value = value

    def func1(self):
        print(f"The value is: {self._value}")

    @property   #getter
    def func2(self):
        print(f"The value using getter is: {self._value}")


m = MyClass("Homealone")
m.func1()
m.func2         #getter


# SETTER
# since getter method is called without using (). that means it does not take any parameters.
# so to take paramters, we have to use SETTER
class MyClass2:
    def __init__(self,value):
        self._value=value

    @property
    def info2(self):
        print(f"The value: {self._value}")

    @info2.setter
    def info2(self,value):
        self.nvalue=value*10
        print(f"Multiple of 10 is: {self.nvalue}")

m2 = MyClass2("Annam")
m2.info2        #calling getter
m2.info2 = 20   #calling setter

# INHERITANCE
class Employee:     #parent class
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def info3(self):
        print(f"Id is: {self.id}, Name is: {self.name}")

class Department(Employee):     #child class    #it will inherit all the properties and attributes of parent class
    def dep(self):
        print("The default language is python")
        print(f"Id is: {self.id}, Name is: {self.name}")

e = Employee(27,"Home")
e.info3()

#we have to pass parameters while calling child class since it inherits from Employee class otherwise it will throw error.
d = Department(15,"yty")    #this parameters are asigned to parent as well as for child class.
d.info3()       #calling inherited parent class function
d.dep()

# Access Modifiers
# There is no public, private, protected thing in python
# By default, everything is public in python.
# But, we can set attribtes as private by adding "__" as a prefix
# we can access that attriute by calling as "_Classname__atributename"
class Modifier:
    def __init__(self):
        self.__name = "Tushar"

m = Modifier()
print(m._Modifier__name)



# STATIC method
# static method is used inside a class and can be called without instance of class

class Main:
    def __init__(self,num,a,b):
        self.num = num
        self.a=a
        self.b=b

    @staticmethod
    def add2(a,b):
        print("Addition:", a+b)

    # ERROR: since its not static
    # def add2(a,b):
    #     print("Addition:", a+b)

    def add(self):
        print("Addition:", self.a+self.b)


m = Main(1000,5,10)
print(m.num)
m.add2(50,10)   #we can pass paramters via function only from using static method
m.add()

# INSTANCE VARIABLE AND CLASS VARIABLE
class Employee:
    company = "Tushar Enterprise"

    def __init__(self,name):
        self.name = name
        self.id = 7

    def info(self):
        print(f"Your name: {self.name} ,ID: {self.id} company: {self.company}")

e = Employee("Tushar")
print(e.company)
print(Employee.company)
e.info()

j = Employee("Aman")
j.info()
j.company = "Google"    #changed value for j instance only.
j.info()
print(Employee.company) #Apple  #since its class variable

# SUPER KEYWORD
# super method is used to follow DRY-(Donot Repeat Yourself) code methodology
class Parent:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        print(f"for Parent; Id: {self.id}, Name: {self.name}")


class Child(Parent):
    def info(self):
        print(f"for Child; Id: {self.id}, Name: {self.name}")

class Child2(Child):
    def __init__(self,id,name,sal):
        # self.id=id
        # self.name=name
        super().__init__(id,name)   #using attributes of __init__ method of parent class
        self.sal = sal
        print(f"for Child2; Id: {self.id}, Name: {self.name}, Salary: {self.sal}")

p = Parent(10,"Aman")
print(p.id)
c = Child(27,"Tushar")
c.info()
# whenever object of child class is created, it will first run init method of parent class and assign variable values and then it will run init method of child class
c2 = Child2(99,"John",5000)
print(c2.id)



# magic or dunder methods
# they are special methods which starts and ends wth "__"
class Emp:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    # def __str__(self):
    #     return f"The name os employee is {self.name}"
    def __repr__(self):
        return f"Employee: {self.name}"

    def __call__(self, *args, **kwargs):
        # print("Hiiiiii")
        for a in args:
            print(a)


e = Emp("Joy")
print(len(e))
# __str__ method is called by printing the object of a class
print(e)    #__str__ method is called, # when str method is commented in code then repr methodd is called.
e("Tushar","Aman",33)   #__call__ method is called

# dir(), __dict__, help()
class Main:
    def __init__(self,id, name):
        self.id = id
        self.name = name
        self.colour = "black"
        print(self.id,self.name,self.colour)

m = Main(10,"Tushar")
print(dir(m))   #it shows all the inbuilt functions and attributes
print(help(m))      #it shows all the attributes and methods defined inside the class
print(m.__dict__)   #it gives all the attributes and its values as a dictionary output format
print(m.__sizeof__())
print(m.__class__)  #class name
# print(m.__delattr__)


# METHOD OVERWRITING
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Area: {self.x*self.y}")

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,x,y):
        # self.x = x
        # self.y = y
        super().__init__(x,y)
        print(f"Area Circle: {self.x*self.y}")

    def area(self):
        return 3.14 * super().area()

s = Shape(10,20)
print(s.area())
c = Circle(2,3)
print(c.area())


class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()





