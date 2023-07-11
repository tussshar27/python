def func1(a,b):
    print("Additon is:",a + b)

def greater(a=5,b=10):     # by default a is 5
    if(a>b):
        print("A is greater than B",a)
    else:
        print("B is greater than or equal to A",b)

func1(10,2)
greater(10,20)
greater()
greater(b=20)
greater(b=7,a=2)


# variable length arguments
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
# The function accesses the arguments by processing them in the form of tuple.
def name(*n):
    print("Hello,", n[0], n[1], n[2])
    print(type(n))       # tuple

name("James", "Buchanan", "Barnes")

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












