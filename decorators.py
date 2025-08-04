A decorator is a function that takes another function as input and returns a new function with modified behavior.

def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

Output:
Something before the function runs
Hello!
Something after the function runs
