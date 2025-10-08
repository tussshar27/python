# code with harry

# everythng in python is object
a = 10
b = 20
print("Addition for a + b is",a+b)


# datatype
a1=10
a2="tushar"
a3=True
a4=None
print(type(a3))
print(type(a4))


#string variable
c="1"
d="2"
print(c+d)  #12
print(c,d)  #1 2

# print()
print("tushar", 2,7,sep="~",end="007")    #sep means (seperated by)
print("tushar", 2,7,sep="~",end="007\n")    #sep means (seperated by)
print("tushar", 2,7,sep="~",end="007")    #sep means (seperated by)

# TypeCasting
#1. implicit Typecasting
# casting is done by python itself internally, it will convert lower order datattype to higher order datattype
b1=1
b2=5.2
print(b1+b2)

#2. explicit Typecasting
# casting is done externally
c1=3
c2="7"
print(c1 + int(c2))


#user input, input fnction
# by default, python will take value from input function as STRING, so use typecasting
# d = input("Enter your name: ")
print(d)

# d1=input("enter nmer1:")
# d2=input("enter nmber2:")
# print(int(d1) + int(d2))


# string, everything which is in double or single quotes in python is consider as string
e1="tushar annam"

# for multiline string use three single quotes otherwise it will give error.
e2='''Hello,
my name is
Tushar Annam'''

# string is like an array
print(e1[0])
print(e1[1])
print(e1[2])
print(e1[3])

# to access multiline string, use for loop
# for in loop

for char1 in e1:
    print(char1)

for char1 in e2:
    print(char1)



# string split
nm="Harry"      #it starts from 0 in any programming lang, and assume end starts from -1.
print(nm[-4:-2])    #compiler thinks [5-4:5-2]
print(nm[:3])
print(nm[0:3])
print(nm[-4:])
print(nm[-2:])

# strings are immutable (can't change)

# string functions
s="!!Tushar!!!! Tushar!!!!!!!!"
print(s)
print(len(s))       #len function is called different from other functions because strings are immutale, so the other functions create another string from main string.
print(s.upper())
print(s.lower())
print(s.rstrip("!"))    # it will strip from end and not from start
#for rstrip: chars/string is an optional argument that specifies the characters to remove. If chars is not specified, all trailing whitespace characters will be removed.

print(s.replace("Tush","Ann"))
print(s.split(" "))     # it will create list with the mentioned delimiter
heading = "introduction tO Strings iN pYThon"
print(heading.capitalize())     # it will uppercase initial letter and lower case everything
print(len(heading))         # 33
print(heading.center(50))   #33+17=50   # it will shift text to center within 50 size as mentioned
print(s.count("Tushar"))    #starts from index 2
print(s.endswith("!!!"))
print(s.endswith("har",2,8))
print(s.find("ush"))        # gives first occurance index
print(s.index("us"))    #index func is similar to find func just that it will throw erro, if it not found where as find will give -1
s1="WelcomeWorld"
print(s1.isalnum())      # retrns TRUE if string has A-Z, a-z, 0-9
s2="Welcome007"
print(s2.isalpha())     # returns true only when there is no numer other than A-Z, a-z
print(s1.lower())       #print new lower string
print(s1.islower())     #print true if stg is lower

s3="Tushar\n"
print(s3)
print(s3.isprintable())
s3="    "
print(s3.isspace())     # returns true if it is space

s3=" Hello world, from Tushar"
print(s3.title())       #makes initial of all capital
print(s3.istitle())         # it sees where all the initial letters are capitalize for title or not.

print(s3.startswith(" Hello"))

print(s3.swapcase())    #makes lowercase upper and uppercase lower

# if else condition
# it works on conditional operator <,>,<=,>=,==,!=
# a=int(input("Enter number for A:"))
# b=int(input("Enter number for B:"))
if(a>b):
    print("A",a)
elif(b>a):
    print("B",b)
else:
    print("A=B",a)

# match case
# it is similar to if-else block.
# there is no need of declaring break statement in case statement where we have to declare break in c/c++ or else it will run all the cases content.

example 1:
# x = int(input("Enter a number"))
x = 10
match x:
    case 0:
        print("x is zero")

    case 1:
        print("x is 1")

    # case _ is the default case in python 10.
    case _ if x!=90:
        print("x is not 90")
    case _ if x!=80:
        print("x is not 80")
    case _:
        print(x)

example 2 match case (if condition):
number = 10

match number:
    case x if x > 0:
        print("Positive number")
    case x if x < 0:
        print("Negative number")
    case _:
        print("Zero")

output:
Positive number


# for in loop
f1 = 'TusharAnnam'
for i in f1:
    print(i)
    if(i == 'A'):
        print("Hi")

f2 = ['apple','banana','grape','orange']
for j in f2:
    print(j)

for j in range(5):  # 0 to 4
    print(j)

for j in range(1,5):  # 1 to 4
    print(j)

for j in range(1,5):  # 1 to 4
    print(j+1)          # 2 to 5

for j in range(1,20,6):  # 1+6, 6 is step
    print(j)

# while loop

i=0
while(i<5):
    print(i)
    i = i + 1
print("Done with the loop")     # same as else block
#
# j = int(input("Enter number:"))
# while(j<30):
#     j = int(input("Enter number:"))
#     print(j)
# else:
#     print("Done with the loop")

# python doesn't have do while loop
# i = 4
# do {
#     # print("Hello")
#     print(i)
#     i = i - 1
# }while(i<5);
#     # print(i)
#     # i = i - 1

# emulation of do while loop
# break and continue statement
i=1
while(True):
    print(i)
    i = i + 1
    if not i < 10:
        break

for i in range(5):
    if i == 3:
        continue
    print(i)

# list
# list in python can be changed, but string and tuple cannot be changed.
l = [1,2,3,"Tushar",True]
print(type(l))
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(type(l[4]))
print(l[-3])
print(l[len(l)-3])
print(l[5-3])
print(l[2])

# if in statement
if "Tushar" in l:
    print(True)
else:
    print(False)

#same thing applies for string
if "Tus" in "Tushar":
    print(True)
else:
    print(False)

print(l[:]) # it will print all content of list

# jump list
print(l[1:5:2])

l1 = [12,23,1,2,4,2,6]
print(l1)
l1.append(7)
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l1.reverse()    #make reverse of list content not sort
print(l1)
print(l1.index(23))     # it will give index of number in list, also it will return the first occurance
print(l1.count(2))
l2 = l1.copy()      #copying list to new list
l2[0]=5             #changing content of a list
print(l1)
print(l2)

l2.insert(2,45)     # it will insert mew
print(l2)
k = l1 + l2         # creating new index by concatenating 2 indexes
print(k)
l1.extend(l2)       #appending l1 with l2
print(l1)

# tuple and string are similar to list, we cant change it like list.
t = (2,3,45,8,34,"Tushar", True, 7)

# all methods in tuple are same as in list, just that yoo can't change tuple
print(len(t))
print(t)
print(type(t))
# t[0] = 10     # error, tuple can't be changed.
print(t[0])
if 45 in t:
    print(True)
else:
    print(False)
t2 = t[0:3]
print(t2)

# we can indirectly make changes in tuple by coverting into list and then again coverting into tuple.
print(t2)
lt = list(t2)
lt.append("Tus")
print(lt)
lt.pop(2)       # it will remove item from index 2
print(lt)
lt[0]=77
print(lt)
t2 = tuple(lt)
print(t2)

t3 = t + t2     # mergng of two tuples and creating a new one.
print(t3)
print(t3.index(3,4,11))     # give index no for 3 from 4th to 11th index


# f-strings
letter = "Hey, my name is {} and I am from {}"
name = "Tushar"
country = "India"
print(letter.format(name,country))

letter = "Hey, my name is {1} and I am from {0}"
name = "Tushar"
country = "India"
print(letter.format(country,name))

# f-string is used to replace above code.
txt = f"Hey, my name is {{name}} and I am from {country}"
print(txt)

price = 49.09999
txt2 = f"hi, price is {price:.2f} dollars!"     # it convert to decimal float
print(txt2)


# docstrings and PEP-8
# docstrng is used to document code
# docstring should be declare just after the function declaration
def square(n):
    '''Takes in nmber n, returns the square of n'''
    # print(n**2)
    return n**2

print(square(10))
print(square.__doc__)   #it prints comment present inside function

# PEP 8
# python enhancement proposal
# it provides guidelines and best practices on how to write python code.

# import this       #run it in python terminal, it will print zen of python PEP8.


# recursion
# a function calling itself in it is known as recursion

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
        # 5*4*3*2*1 = 120

print(factorial(5))


def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# 0 1 1 2 3 5 8 ....
print(fibonacci(10))


# sets
# set is made so that there can't be duplicate data in it.
# set is unordered collection of data items
s = {2,4,2,6,6}         # {2, 4, 6}
print(s)

if 2 in s:
    print(True)
else:
    print(False)

s2 = {True, "Tushar", 27, 98}
print(s2)

for i in s2:    # to iterate individual element of set
    print(i)


s3 = {}
print(type(s3))     #it will by default take empty set as dictonary.

s4= set()           #we have to mention set keyword if its empty.
print(type(s4))

# set methods
s1 = {2,3,2,5,9,8,3}
print(s1)
s2 = {6,5,7,2,3}
print(s2)
print(s1.union(s2)).  #it combines unique values of S1 and S2 and create new set if we want
s3 = s1.update(s2).   #it will update existing values of S1 set.
print(s3)

print(s1)
print(s2)
print(s1.intersection(s2))  #intersect
print("s1",s1)

print(s1.intersection_update(s2))
print("s1",s1)

print(s1.symmetric_difference(s2))

print(s1.isdisjoint(s2))

print(s1.issuperset(s2))

print(s1.issubset(s2))

s1.add("Tushar")
print(s1)

# remove raise error while discard does not raise any error.
s1.remove("Tushar")
print(s1)

s1.clear()      # this will clear all the elements in set
print(s1)

del s1  # it will delete whole set
# print("s1",s1)

# dictionaries
# access is fast
# used to create mapping
# they are ordered

d = {'name': 'Tushar', 'age': 24, 'eligible': True}
print(d)
print(d['name'])    # if name is not there then it will throw error.
print(d.get('name'))  # if name is not there then it will throw none

print(d.keys())
print(d.values())

for key in d.keys():
    print(key)

for key in d.keys():
    print(f"The value to key {key} is {d[key]}")

print(d.items())

for key, value in d.items():
    print(f"The key {key} has value {value}")

emp = {12: 45, 34: 34, 6: 78, 87: 98}
emp2 = {223: 56, 887: 23}

emp.update(emp2)
print(emp)

emp.pop(34)
emp.clear()
del emp

# for  - else loop
# else block will run after for loop completely running.
# we can also use else block with while loop.

for i in range(5):
    print(i)
else:
    print("for loop is completed.")

# while - else loop

i = 0
while(i<5):
    print(i)
    i = i + 1
else:
    print("while loop is completed.")


# excepton handling
# try - except

try:
    # a = int(input("Enter number:"))
    a = 10
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except Exception as e:
# except:     # work same as above
    # pass
    print(e)

except ValueError:
    pass
except IndexError:
    pass
except ArithmeticError:
    pass

print("after try except block")

# finally block
# finally block will always executed
def fin():
    try:
        l = [1,4,5,3,7]
        # i = int(input("Enter number:"))
        i=9
        print(l[i])
        return 1
    except:
        print("invalid index")
        return 0
#print("it will also get exeuted but not in function, thats why we use finally block and that is the main use of it")
    finally:
        print("I am always executed.")

print(fin())


# inbuilt exception

# a = int(input("Enter number between 5 and 10:"))
# if(a<5 or a>10):
#     raise ValueError("Value should be between 5 and 10")

# short hand if-else statement
a = 10
b = 20
print("A") if a > b else print("=") if a == b else print("B") if a < b else ""

c = 27 if a < b else 0
print(c)


# enumerate function

marks = [1, 12, 45, 5, 32, 28, 30]

index = 0
for mark in marks:
    print(mark)
    if index == 3:
        print("Tushar!")
    index += 1

print("///////////////////////////////////////////")
# by using enumerate function, we can stop declaring or incrementing temp variable such as index
for index, mark in enumerate(marks):
    print(mark)
    if index == 2:
        print("After index 2")

print("///////////////////////////////////////////")
# by default index starts at 0
# we can change that using start parameter

for index, mark in enumerate(marks, start=1):
    print(mark)
    if index == 2:
        print("After index 2")


print("///////////////////////////////////////////")

# virtual environment in python
# py - m venv myenv                 #to create
# myenv\Scripts\activate.ps1        #to activate, #use ps1 in powershell
# source myenv/bin/activate         #for lnux, mac
# deactivate                        #to deactivate
# pip freeze                        #to know the installed package versions
# pip freeze > requirements.txt     #creating requrement fle
# pip install -r requirements.txt           #to install the packages in other venv.


# how to import packages in python

import math
# result = math.sqrt(2)
# print(result)
print(dir(math))    #this will prnt all the fnctons and variables availale in math package.


from math import sqrt, pi
# result = sqrt(2)
# print(result)


# from math import sqrt as s, pi
# result = s(2) * pi
# print(result)


from tushar import welcome, tush    #can import from other file
# from tushar import *    #can import from other file
welcome()
print(tush)


# --------------------

# __name__ == "__main__"

# name is set to main, when you run program without importing other python script.
import tushar       #just by importing tushar,tushar.py file will run
tushar.welcome1()
print(__name__)


# os module
import os

if(not os.path.exists("data")):
    os.mkdir("data")

# for i in range(1,10):
#     os.mkdir(f"data/day{i}")


# for i in range(1,10):
#     os.rename(f"data/day{i}",f"data/tutorial{i}")

folders = os.listdir("data")
print(folders)

for folder in folders:
    print(os.listdir(f"data/{folder}"))

print(os.getcwd())
os.chdir("data")
print(os.getcwd())
# os.remove("")


# local and global variable
# a local variale is a variable which is defined in a function
# were as, global variable is a variable which is defined outside the function or can be declared inside a function but using global keyword and can be accessed anywhere.

x = 5

def myfunc():
    global x.           #tells py to use global x instead of creating a new local var.
    x = 10
    y = 15
    print(x)

print(x)
myfunc()
print(x)    #x value is changed to 10 bcoz of global declared in fuunction


# file IO in python
# r = read, w = write, a = append
print(os.getcwd())
os.chdir("../")
print(os.getcwd())

# Reading a file
f = open('myfile.txt', 'r')
print(f)
print(f.read())
f.close()   #not mandatory in read mode, but a good practise to close file at the end.

# writing a file
# two types: overwrite (w) and append (a)

# write
f = open('myfile.txt','w')
f.write("HEllo Tushar!!!!")
f.close()

# append
f = open('myfile.txt','a')
f.write("\nThis is second line")
f.close()


# 'with' statement
# by using 'with' there is no need of close function to used.
# 'with' can be used with r , w , a

with open('myfile.txt','r') as f:
    print(f.read())

# readline() method
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.
# The readlines() method reads all the lines of the file and returns them as a list of strings.
f = open('myfile.txt','r')  #double quotes can be used

while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()


# writeline() method
# f = open('myfile.txt', 'w')     # we can also use 'a', which will append the content in a file
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()
#
# f = open('myfile.txt','a')
# lines = ['abc','pqr','mno']
# for line in lines:
#     f.writelines(line + '\n')
# f.close()

with open('myfile.txt','r') as f:
    print(type(f))
    f.seek(5)
    print(f.tell())     #it will tell where the seek is.
    data = f.read(10)   #it will read the next 10 char
    print(data)
#
# with open('myfile.txt', 'a') as f:
#     f.write("Hello world!")
#     f.truncate(12)  #it will keep content till 12 chars and will remove all after it.


# lambda functon is a anonymous function
# lambda function is only useful if we have one liner code.
def cube(x):
    v = x * x * x
    print(v)
cube(10)

# below lambda functon works same as above function code.
cube1 = lambda x: x * x * x
avg = lambda x,y,z: (x+y+z)/3
print(cube1(5))
print(avg(5,4,3))

# by using lambda, we can pass function as an argument
def appl(fx,value):
    return 6 + fx(value)

# print(appl(cube,2))         #error
print(appl(cube1,2))


# MAP

# map, filter and reduce  built-in functions
# they are also known as high order function because they take other functions as a argument

def cube(r):
    return r*r*r

print(cube(5))

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

# by using map function, we can write above code in more efficient way.
# we use map function and pass the function and list.
newnewl = list(map(cube,l))   #we have to convert map object into list
newnewl = list(map(lambda x: x*x*x,l))  # we can also use lambda functon
print(newnewl)

# FILTER
def filter_func(a):
    return a > 2
# above function will return True or False
# filter fnction will filter elements which are greater than 2
newnewl = list(filter(filter_func,l))
print(newnewl)

# REDUCE
# we have to import reduce to use it.
from functools import reduce
num = [1,2,3,4,5]
num = [1,2,3,4,5]
      # 3,3,4,5
       # 6,4,5
        # 10,5
         # 15   #final output for reduce function
def mysum(x,y):
    return x + y

sum = reduce(mysum,num)
print(sum)

# is vs ==
# is compares exact memory location where as == compares values.

a = 4
b = "4"

print(a is b)   #False
print(a == b)   #False

c = [1,4,23]
d = [1,4,23]

print(c is d)   #False
print(c == d)   #True

e = 4
f = 4
# since 4 is immutable, python stores in same memory locaton.
print(e is f)   #True
print(e == f)   #True


# class and object
class Person:
    name = "Tushar"
    occupation = "Software Engineer"
    networth = 10

    # NOTE: we have to mandatorily define self argument in a method , if the function is defined in a class
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()        #a object is created.
print(a.name,a.occupation)     #calling variable
a.info()            #calling function

b = Person()        #b object is created
b.name = "Aman"
b.occupation = "Businessman"
b.info()

c = Person()
c.name = "Naman"
c.occupation = "Artist"
print(c.name," ,",c.occupation)
c.info()


# constructor
# Constructors are generally used for instantiating an object.
# The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
# In Python the __init__() method is called the constructor and is always called when an object is created.
# the above code can written using constructor
# __init__(self) is a special method used to build constructor
class Person:
    def __init__(self):     # default constructor
        print("Hey I am a person")

a = Person()    # whenever object is created, constructor is called by default
b = Person()

class Person2:
    def __init__(self,n ,o):    #parametiresed constructor
        self.name = n   #name variable is declared here in constructor
        self.occ = o    #occ variable is declared here

    def info(self):
        print(f"{self.name} is a {self.occ}")

a1 = Person2("Tush","Engineer")
b1= Person2("Apr","Doctor")
# c1 = Person2()    #it will give TypeError: Person2.__init__() missing 2 required positional arguments: 'n' and 'o'
a1.info()
b1.info()
a1.info()


# DECORATOR
# a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.
# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.
# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function.

def greeting(hello):     #hello function is passed as an argument
    def modfunc():      #new function is created.
        print("Good Morning")
        hello()      #below hello function is called
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


class Empl:
    def __init__(self):
        self.__name = "TUSHAR"

e = Empl()
print(e._Empl__name)    #name mangling
print(e.__dir__())      # to view all the methods available for this object
print(dir(e))           # obj.__dir__() and dir(obj) both are the same
print(dir(Empl))

# PROTECT: There is only naming convention for protected attribute ie "_" as a prefix. mind that its no use for protect and its just a naming convention.


# snake, water and gun game
# import random
# u = int(input("Enter 0 for snake, 1 for water and 2 for gun:"))
# c = random.randint(0,2)
#
# def check(u,c):
#     if u == c:
#         return 0
#     elif (u == 0 and c == 1):
#         return -1
#     elif (u == 1 and c == 2):
#         return -1
#     elif (u == 2 and c == 0):
#         return -1
#     else:
#         return 1
#
# check(u,c)
# print("user:",u)
# print("computer:",c)
#
# if check(u,c) == 0:
#     print("its a draw")
# elif check(u,c) == 1:
#     print("you won")
# else:
#     print("you lose")


# Book game exercise
class Library:
    book = []
    no_of_books = 0
    def addBook(self,name):
        self.book.append(name)
        self.no_of_books += 1
        print(self.book)
        print(f"Number of books: {self.no_of_books}")
        self.checkCount()

    def checkCount(self):
        if self.no_of_books == len(self.book):
            print("Book count is matched!")
        else:
            print("Book count is not matched")
obj = Library()
obj.addBook("Maths")
obj.addBook("Bio")
obj.addBook("Phy")
obj.addBook("Chem")


# Static method
# static method is used inside a class and can be called without instance of class
class Main:
    def __init__(self,num):
        self.num = num

    # there is no need of mentioning self inside add func. since its staticmethod
    @staticmethod
    def add(a,b):
        return a + b

o = Main(50)
print(o.num)
print(o.add(5,10))
print(Main.add(5,10))   #we can also call it using class name.


# instance variable and class variable
# In Python, variables can be defined at the class level or at the instance level.
# Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class.
# Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class.

class Employee:
    companyName = "Apple"   #class variable
    def __init__(self,name):
        self.name = name    #instance variable
        self.amount = 10.0  #instance variable

    def info(self):
        print(f"{self.name} works in {self.companyName}")

obj1 = Employee("Tushar")
obj1.info()
print(Employee.companyName)
obj2 = Employee("Aman")
obj2.companyName = "Google"
obj2.info()
print(obj2.companyName)     #first, it will check if instance variale is asigned, and if not then it will show class variable
print(Employee.companyName)


# class method
# To define a class method, you simply use the "@classmethod" decorator before the method definition. The first argument of the method should always be "cls," which represents the class itself.

class Emp:
    company = "Apple"

    def info(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls,newCompany):
        cls.company = newCompany

o = Emp()
o.name = "Tush"
o.info()
print(Emp.company)
o.changeCompany("Tesla")
print(Emp.company)


# class method as alternative constructor
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls,string):
        # return cls(string.split("-")[0],int(string.split("-")[1]))
        # below code is same as above
        name, salary = string.split("-")
        return cls(name,int(salary))

e = Employee("Tushar",10000)
print(e.name)
print(e.salary)

string = "Aman-12000"
e2 = Employee(string.split("-")[0],string.split("-")[1])
print(e2.name)
print(e2.salary)

string = "Arya-15000"
e3 = Employee.fromStr(string)
print(e3.name)
print(e3.salary)


# dir(), __dict__, help()
class Dir:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.version = 1

d = Dir("Tush",1000)
print(d.__dict__) #it converts into dictionary
print(dir(d))
print(help(d))


# super keyword
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

    def __str__(self):
        return f"The name os employee is {self.name}"
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


# method overriding
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,r,n):
        self.r = r
        self.n = n
        super().__init__(r,n)       #calling above init

    # to make use of above area function with super, we have to use above init function as well..
    def area(self):
        return 3.14 * super().area()    #calling above superclass area function

s = Shape(3,4)
print(s.area())
c = Circle(10,20)
print(c.area())


# os module exercise
import os

# to rename a file in a directory from test.md to demo.md
# os.rename("data/tutorial5/test.md","data/tutorial5/demo.md")

dirs = os.listdir("data")
i = 1
for dir in dirs:
    # os.rename(f"data/{dir}",f"data/{i}")
    i = i + 1


# operator overloading
# refer this article: https://www.geeksforgeeks.org/operator-overloading-in-python/
# Here, We defined the special function “__add__( )”  and when the objects ob1 and ob2 are coded as “ob1 + ob2“, the special function is automatically called as ob1.__add__(ob2) which simply means that ob1 calls the __add__( ) function with ob2 as an Argument and It actually means A .__add__(ob1, ob2).


class A:
    def __init__(self,a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

obj1 = A(5)
obj2 = A(10)
obj3 = obj1 + obj2
print(obj3)
print(obj2.__add__(obj1))   #same as above
print(A.__add__(obj1,obj2)) #same as above


# single inheritance
# recheck the code
class Animal:
    def __init__(self,a):
        self.a = a

    def sound(self):
        print(f"{self.a} makes sound.")

class Cat(Animal):
    # def __init__(self,a):
    #     self.a = a

    def sound(self):
        super().sound()
        print(f"{self.a} makes sound.")

ob = Animal("Dog")
ob.sound()
ob2 = Cat("Catt")
ob2.sound()


# multiple inheritance
# it has one child class and more than one parent classes

class Employee:
    def __init__(self,name):
        self.name = name

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class EmployeeDancer(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name

e = EmployeeDancer("Shivani","Kathak")
d = Dancer("abc")
print(e.name)
print(e.dance)
print(d.dance)
d.show()
print(EmployeeDancer.mro())


# multilevel inheritance
#CLASS:  A -> B -> C
# a derived class inherits from another derived class.

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def details(self):
        print(f"Name: {self.name}, Species: {self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def details(self):
        Animal.details(self)
        print(f"Breed: {self.breed}")

class GoldenRetriver(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="GoldenRetriver")
        self.color = color

    def details(self):
        Dog.details(self)
        print(f"Color: {self.color}")

g = GoldenRetriver("Man","Black")
g.details()











