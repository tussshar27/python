# if we write "return" inside a function then in order to use it, we need to use print() to call the function or it can be used in other calculation like a variable
# return is not mandatory in function, means we can use or call a function without mentioning return in it.
def func0(a,b):
  print(f"a + b: {a+b}")

func0(10,20)

def func1(a,b):
    print("Additon is:",a + b)
    print(f"a + b: {a+b}")
    return f"{a+b}"

calc = func1(10,20)

print(calc)

def greater(a=5,b=10):     # by default a = 5, b = 10
    if(a>b):
        print("A is greater than B",a)
    else:
        print("B is greater than or equal to A",b)

print(func1(10,2))
greater(10,20)
greater()    #it will pick the default values which are passed as parameters
greater(b=20)
greater(b=7,a=2)


# variable length arguments
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
# The function accesses the arguments by processing them in the form of tuple.

# what is tuple?
# tuple is ordered and immutable (unchangeable). it is a collection used to store multiple items in a single variable.
fruits = ("apple", "banana", "mango")
print(fruits)

def name(*n):
    print("Hello,", n[0], n[1], n[2])
    print(type(n))       # tuple

name("James", "Buchanan", "Barnes")

def func3(*n):
  print(f"n values are: {n[0]}, {n[1]}")
  print(type(n))


t1 = ('tushar','annam')
func3(*t1)

# return
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))

#  The function accesses the arguments by processing them in the form of dictionary.
def name(**n):
    pass
    print("Hello,", n["fname"], n["mname"], n["lname"])
    print(type(n))       # dictionary

name(mname = "Buchanan", lname = "Barnes", fname = "James")

def p(**pn):
    print("Hey,",pn["p1"],pn["p2"])

p(p1="Tushar",p2="Annam")   # passin key value pair dictionary

def pt(*pt2):
    print("Hi,",pt2[0],pt2[1])

pt("ABC","PQR")     # tuple












