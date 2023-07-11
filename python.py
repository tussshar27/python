# a = 10      #no need to declare datatype for variable in python
# b = 12.70   #no ; is required
# c = "Heyyyyy"
# d = True
# print("Hello World")
# print(a)
# print(b)
# print(c)
# print(d)

# #taking user input from console
# name = input("What's your name? ")  #taking input from user
# print("Hello " + name)

# birth_year = input("Enter your birth year: ")   #user input is always in String in python
# age = 2021 - int(birth_year)    #converting String to int using inplicit type conversion
# print(age)      #inplicit type convertsions are int(), float(), bool(), str()

# first = input("Enter first number:")
# #first = float(input("Enter first number:"))
# second = input("Enter second number")
# cal = float(first) + float(second)
# print("sum: " + str(cal))   #converting cal to string due to using of sum:

print("tushar", 2,7,sep="~",end="007\n")

#logical operator - True/False
price = 15
print(price > 10 and price < 20)
print(price > 10 or price > 20)
print(not price > 10)


#if statement
temperature = 250
if(temperature > 30):
    print("It's too hot drink plenty of water")
    print("Don't go outside")

elif(temperature > 20):
    print("it's a nice day")

elif(temperature > 10):
    print("It's a bit cold")
else:
    print("It's too cold")

# #if statement exercise
# weight = float(input("Enter weight: "))
# unit = input("Enter K for kg or L for lbs:")
# if(unit.upper() == "K"):
#     print("Weight in kgs" + str(weight * 0.45)) #can only concatenate str (not "float") to str
# else:
#     print("Weight in lbs:" + str(weight / 0.45))

#while loop
i = 1
while i <= 10:
    print(i * '*')
    i = i + 1   #i++ or i-- is not supported in python
print(60 * '#')
print(5 * '*')

# #list - they are changeable(mutable)
# names = ["tom", "harry", "sam", "jam", "gam"]
# print(names)
# print(names[0])
# print(names[-1])    #-1 only works in python returns last element of list
# print(names[-2])    #-2 returns second last element
# print(names[0:3])   #start with 0 index and ends at 2 index excluding 3
# print("####################################################")

#array
numbers2 = [1, 2, 3, 4, 5]
numbers2.append(6)
print(numbers2)

numbers2.insert(0, -1)  #inserting -1 in 0th index
print(numbers2)

numbers2.remove(3)
print(numbers2)

print(2 in numbers2)

numbers2.clear()
print(numbers2)
print(len(numbers2))    #length
print("####################################################")

#for loop and while loop
num = [1, 2, 3, 4, 5]
for item in num:
    print(item)
print("####################################################")

i=0
while i < len(num):
    print(num[i])
    i = i + 1
print("####################################################")

#range() function
for item in range(5):
    print(item)
print("####################################################")

for item in range(2, 10):
    print(item)
print("####################################################")

for item in range(2, 10, 3):
    print(item)
print("####################################################")

#tuple - they are unchangeable(immutable) and are in round braces
num2 = (1, 2, 3)
print(num2)     #note append or insert func are not worked with tuples

# ####################################################
# # select above code and type cntrl+/
# ##################################################### 


# ####################################################################################################

# #GUVI PYTHON WEBINAR

# To open python terminal enter py in cmd

print("hello world!")

# 1) Numbers:   No return type with variable name.
# numbers are of 3 types in python:
# 1. int
# 2. float
# 3. complex

x = 7       #int - can be + or - whole number but not decimal
y = 22.0    #float
z = 5j      #complex - Note: only j is used and its an imaginary number

# String
m = 'johnny'

print(type(x))
print(type(y))
print(type(z))
print(type(m))

# 2) Type convertion:

# int to float
a = float(x)

# float to int
b = int(y)

# int to complex
c = complex(x)  

# int to String
d = str(b) 

print(a)
print(b)
print(c)    #o/p: (7+0j)
print(d)    #o/p: 22

# 3) Operators:
# addition +
# subtraction -
# multiplication *
# division /
# modulus %
# exponential ** (raise to)
# floor division //

m = 10
n = 20
print(m+n)
#############################################################################################
# 4) Types of Errors in python:

# 1. Syntax error:
# >>> print "hello!"
#   File "<stdin>", line 1
#     print "hello!"
#           ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello!")?

# 2. Index error: (its based on the List or array)
# >>> list = [1, 2, 3]
# >>> list[0]
# 1
# >>> list[3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

# 3. Module n not found error:
# >>> import os
# >>> import notmodule
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'notmodule'

# 4. Key error (based on dictionary)
# >>> dic = { '1':'abc', '2':'pqr'}
# >>> dic['1']
# 'abc'
# >>> dic['3']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: '3'

# 5. Import error:
# >>> from math import cube
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'cube' from 'math' (unknown location)

# 6. Stop iteration error: (used on Python iter() Function)
# >>> i = iter([1,2,3])
# >>> next(i)
# 1
# >>> next(i)
# 2
# >>> next(i)
# 3
# >>> next(i)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# 7. Type error: (str cnannot be concatenated with int or any other datatype)
# >>> print('123' + 456)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

# 8. Value error:
# >>> int('xyz')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'xyz'

# 9. Name error: (A variable which is not defined and called is call name error)
# >>> list
# [1, 2, 3]
# >>> i
# <list_iterator object at 0x000000EF9F340AF0>
# >>> abc
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'abc' is not defined

# 10. Zero division error:
# >>> print(100/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero


# 11. Keyboard interrupt error:
# >>> name = input('Enter your name')
# Enter your name                   (*typing cntrl+c*)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyboardInterrupt
#############################################################################################





# 5) variable and printing
#give variable name based on what will be its value.
#eg: big box with its contains list on top of the box
myName = "Tushar Annam"
print(myName)

myAge = 23
print(myAge)

x = 5
x = 'john'
print(x) #op: john

# initializing multiple variables in same line.
m,n,o = 'apple','ball','cat'
print(m)
print(n)
print(o)

# assigning multiple variables to one value.
a=b=c = 'orange'
print(a)
print(b)
print(c)

# 6) Strings
s1 = 'eminem'
s2 = "hiphop"

# multiline string
s3 = """Hey there!,
This is Tushar Annam,
From MCA."""

print(s1)
print(s2)
print(s3)

# String is an array in python. That means, we can access any character just like an array
x = "Hello, from the World!"
print(x[0])
print(x[4])

# looping string just like an array
for a in x:
    print(a)
    
# len() function in string
print(len(x))

# using in
print('the' in x)   #gives Boolean value.

# slicing
print(x[3:5])   #printing from 3nd index to 4ht index
print(x[:5])    #printing from start i.e 0th to 4th index
print(x[3:])    #printing from 3nd index to the end
print(x[-5:-2]) #printing from 2nd index from last to 4th index

# converting to uppercase and lowercase string
print(x.upper())    #op: HELLO, FROM THE WORLD!
print(x.lower())    #op: hello, from the world!

# strip() function used to remove white spaces in starting and ending of word/sentence and not middle of it.
m = "   Hello, world   "
print(m)
print(m.strip())

# replace() used to replace string characters
print(m.replace('H','Y'))
print(m.replace('He','Y'))

# IMPORTANT: split() used to split the strings into list
print(m.split(','))     #op: ['   Hello', ' world   ']      #, becomes the divider
print(m.split('o'))     #op: ['   Hell', ', w', 'rld   ']   #o becomes the divider

# concatenate strings
a = "Hello"
b = "World"
print(a+b)      #op: HelloWorld
print(a+ " " +b)    #op: Hello World

# a. String methods

# b. Escape characters
# An escape character is a backslash \ followed by the character you want to insert.
txt = " \"Tushar\" \"Annam\" "
print(txt)  #op:  "Tushar" "Annam"

# format()
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1) #op: My name is John, I'm 36
print(txt2) #op: My name is John, I'm 36
print(txt3) #op: My name is John, I'm 36

#2. condition
x = 50
if x > 60:
    print("Your number is above 60")
elif x == 60:
    print("Your number is equal to 60")
else:
    print("Your number is below 60")
    
# and condition
a = 10
b = 20
if a>5 and b<50:
    print('yes')
else:
    print('No')
    
# or condition
a = 10
b = 20
if a>5 or b<50:
    print('yes')
else:
    print('No')
    
# 7) Functions
def myfunc():
    print("Hello!!!")
    return "a"
myfunc()

def myfunc2(x): #here, x is parameter
    print(x+ " world")
myfunc2("Hello")    #here, "Hello" is argument

def myfunc3(x,y):
    print(x+ " " +y)
myfunc3("Black","White")

# 7) loop- There are only two loops in python i.e for - in and while
# for-in loop
marks = [1, 2, 34, 47, 54, 67, 45, 30, 75]  #list
for i in marks:
    if i < 50:
        print(i)
        
# same for String
str = "Hello"
for s in str:
    print(s)
    
# break statement
mk = [1, 2, 34, 47, 54, 67, 45, 30, 75]  #list
for i in mk:
    print(i)
    if i == 54:
        break
    
# continue statement
# break statement
mk2 = [1, 2, 34, 47, 54, 67, 45, 30, 75]  #list
for i in mk2:
    if i == 54:
        continue
    print(i)
    
# range function
for r in range(20): 
    print(r)    #it will print from 0 to 19
    
for r in range(12,20): 
    print(r)   #it will print from 12 to 19

i = 1
while(i<=6):
    print(i)
    i += 1  #i=i+1
    
    
# 8) functions as arguments
# NOTEe: when passing the function, () parantheses is not used. while calling the function, ()  is used. 
list = ['car','bike','truck','scooter']
def myfunc(x):
    print(x*3)
    
myfunc(list)
    
def mapfunc(myfunc,list):   #passing the myfunc
    for i in list:
        myfunc(i)       #calling the myfunc, so now myfunc will get executed
        
mapfunc(myfunc,list)    #passing the myfunc
    
# There are four types of variables in python which are
# used to store collection of data i.e list, tuple, dictionaries and set.

# 9) list - [] is used -  Ordered, CHANGEABLE, allow duplicates
#list index starts with 0
list = ["Tushar Annam", 92, 89, 94, 87, 87, 75.10, True]
print(list)
print(len(list))
print(list[1])    #accessing single index item of list
print(list[2:5])    
print(type(list))
list[0] = "hey, there"    #replacing item in list
print(list)
list[1:3] = "orange","gauva"
print(list)

list.insert(3,'third')    #insert function is used to insert extra value in a certain or specified position
list.append('last')       #append function is used to add extra value in the last of list
print(list)

# remove function() - used to specified remove item from list
list.remove(75.1)
print(list)

#printing each value of list individually
for i in list:
    print(i)

a = "abcjrkn"   #string
print(len(a))

# 10) tuple - () is used - Ordered, UNCHANGEABLE, allow duplicates
# all operations are same as list just that its unchangeable that means you can't use insert, append function.
tuple = ("Tushar Annam", 92, 89, 94, 87, 87, 75.10, 75.10, True)
print(tuple)
print(type(tuple))
print(type(tuple))
print(tuple[2])

tuple2 = (27,)  #if single value is present then comma must contain in tuple else it will show as string type
print(type(tuple2))

# since tuple is unchangeable we can change the items of tuple by converting to list 
# and changing the item and then again converting to tuple.

# getting error below
a = (10, 'apple', 30, 'banana')
# print(a)
b = list(a)
b[0] = 500
# print(b)
ab = tuple(b)
print(ab)
################################

# 11) Dictionaries - key:value pair - Unordered, Changeable,
# NO duplicates(overwrites existing value with new value of same key)
dictt = {
    'name':'tushar',
    'age':23,
    'vehicle':'bullet',
    'dob':True,
    'fruits':['oranges', 'apple', 'banana'] #list can also be stored as value for key in dictionaries.
}
print(dictt)
print(len(dictt))
print(type(dictt))

#getting the value of key vehicle
x = dictt['vehicle']  
print(x)    #op: bullet

# get() function
x = dictt.get('vehicle')   #2nd method to get the value.
print(x)    #op: bullet

#changing the value.
dictt['vehicle'] = 'honda'  
print(dictt)

dictt.update({'name':'TUSHAR'}) #2nd method to update value
print(dictt)

# add new key-value in dictionaries
dictt['colour'] = 'Black'
print(dictt)

# pop method to remove the key-value pair
dictt.pop("vehicle")    #vehicle key and its value will be removed.
print(dictt)

# 13) List Comprehension
fruits = ['apple', 'banana', 'kiwi', 'grapes']
newfruit = []

for x in fruits:
    if "a" in x:
        newfruit.append(x)

print(newfruit) #op: ['apple', 'banana', 'grapes']

# for string
str = "abcdeaafg"
for i in str:
    if "a" in i:
        print(i)

# 14) File Handling
# There are four modes in file handling and they are: create, read, write, append.
# read mode to file
f = open("trial.txt","r")   #r means read mode

for i in f: #each line represents i
    print(i)
print(f.readline()) #it reads the first line of file
print(f.readline()) #it reads the next line of file
print(f.readline()) #it reads the next line of file
print(f.readline(8)) #it reads the next line of file with 8 characters
print(f.read(10))   #10 is the number of characters we want to read from trial file

f.close()   #after opening we must have to close the file.

# append mode to file
f = open('trial.txt','a')   #a means append which means inserting in last of file.
f.write("this is last line")
f.close()

f = open('trial.txt','r')
print(f.read())
f.close()

# write mode to file
f = open('trial.txt','w')   #w means write mode
# in write mode the below present line overwrites all the existing lines of file
f.write("This is the only line present as it has overwritted all the previous lines")
f.close()

f = open('trial.txt','r')
print(f.read())
f.close()

# create mode to file
f = open('newfile.txt','x') #x means creating a new file, we can also use w for creating new file.
f.close()

# deleting file
import os
os.remove('newfile.txt')



# 15) Class and objects
class Human:
    x=5

h1 = Human()    #h1 object of class
print(h1.x)


#5. pip - package manager for python
#python have multiple different inbuilt packages which can be used by importing them to our program.
#eg: numPy, pandas, scipy, etc.

#6. pickling - Serialize/De-serialize
#converts any variable, list or any objects to Bytes(i.e 0 , 1)
#it is used to make machine run fast. since, machine understands 0s and 1s



