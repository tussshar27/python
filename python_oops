class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def my_func(self):
        print(f'my car is of {self.brand} and model is {self.model}')
        
        
my_car = Car("TATA","SIERA")
print(my_car.brand)     #accessing the variable
print(my_car.model)
print(my_car.my_func())
        
output:
TATA
SIERA
my car is of TATA and model is SIERA
None

=== Code Execution Successful ===

Q. create an ElectricCar class that inherits Car class and has an additional attribute battery_size.
INHERITANCE

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def my_func(self):
        print(f'my car is of {self.brand} and model is {self.model}')
        
       
       
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand=brand
        # self.model=model
        super().__init__(brand,model)       #calling __init__ thats why no need of self
        self.battery_size = battery_size
        
my_electric_car = ElectricCar('Tesla','Model X','85kWh')
print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.my_func())

output:
Tesla
Model X
my car is of Tesla and model is Model X
None

=== Code Execution Successful ===

Q. Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method to access it.
ENCAPSULATION
So we have to make the brand attribute as private. in different language we can declare attribute as a private 
but in python, we have to give __ as prefix to attribute in order to make it private but note that the object cannot access this attribute from outside 
but we can access the private attribute within class since it is private so in order to access it we will use getter method.

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        
    def my_func(self):
        print(f'my car is of {self.__brand} and model is {self.model}')
        
    def get_brand(self):        #getter method
        return self.__brand + ' !!'
       
       
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand=brand
        # self.model=model
        super().__init__(brand,model)   #calling __init__ thats why no need of self
        self.battery_size = battery_size
        
my_electric_car = ElectricCar('Tesla','Model X','85kWh')
print(my_electric_car.model)
print(my_electric_car.my_func())
# print(my_electric_car.__brand)    #we cant access this private attribute from object but we can access it through getter method.
print(my_electric_car.get_brand())

output:
Model X
my car is of Tesla and model is Model X
None
Tesla !!

=== Code Execution Successful ===

Q. Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
POLYMORPHISM
NOTE: python is smart enough to know which method should be called while printing with object.
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        
    def my_func(self):
        print(f'my car is of {self.__brand} and model is {self.model}')
        
    def get_brand(self):        #getter method
        return self.__brand + ' !!'
       
    def fuel_type(self):        #polymorphism
        return 'Petrol or Diesel'
       
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand=brand
        # self.model=model
        super().__init__(brand,model)   #calling __init__ thats why no need of self
        self.battery_size = battery_size
        
    def fuel_type(self):            #polymorphism
        return 'Electric charge'
        
        
my_electric_car = ElectricCar('Tesla','Model X','85kWh')
print(my_electric_car.model)
print(my_electric_car.fuel_type())


my_car = Car("TATA","SIERA")
print(my_car.fuel_type())

output:
Model X
Electric charge
Petrol or Diesel

=== Code Execution Successful ===

Q. Add a class variable to Car that keeps track of the number of cars created.
CLASS VARIABLE
class Car:
    total_car = 0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        # self.total_car += 1   #we can use self as well
        Car.total_car += 1  #class variable
        
    def my_func(self):
        print(f'my car is of {self.__brand} and model is {self.model}')
        
    def get_brand(self):        #getter method
        return self.__brand + ' !!'
       
    def fuel_type(self):        #polymorphism
        return 'Petrol or Diesel'
       
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand=brand
        # self.model=model
        super().__init__(brand,model)   #calling __init__ thats why no need of self
        self.battery_size = battery_size
        
    def fuel_type(self):            #polymorphism
        return 'Electric charge'
        
        
my_electric_car = ElectricCar('Tesla','Model X','85kWh')
print(my_electric_car.model)
print(my_electric_car.fuel_type())


my_car = Car("TATA","SIERA")
print(my_car.fuel_type())

Car("TATA","NEXON")

print(my_car.total_car)
print(Car.total_car)
        
output:
Model X
Electric charge
Petrol or Diesel
3
3

=== Code Execution Successful ===

Q. Add a static method to the Car class that returns a general description of a car.
STATIC METHOD - a method that belongs to a class rather than an instance of a class.
creating static method using DECORATORS.
DECORATORS - used to enhance the functionality of function.
NOTE: since we are accessing the static method with class and not its instance so we will remove self from the parameter.
class Car:
    total_car = 0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        # self.total_car += 1   #we can use self as well
        Car.total_car += 1  #class variable
        
    def my_func(self):
        print(f'my car is of {self.__brand} and model is {self.model}')
        
    def get_brand(self):        #getter method
        return self.__brand + ' !!'
       
    def fuel_type(self):        #polymorphism
        return 'Petrol or Diesel'
        
    @staticmethod                   #decorator
    def general_description():      #static method
        return 'Cars are means of transport'
       
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand=brand
        # self.model=model
        super().__init__(brand,model)   #calling __init__ thats why no need of self
        self.battery_size = battery_size
        
    def fuel_type(self):            #polymorphism
        return 'Electric charge'
        
        
my_electric_car = ElectricCar('Tesla','Model X','85kWh')
print(my_electric_car.model)
print(my_electric_car.fuel_type())


my_car = Car("TATA","SIERA")
print(my_car.fuel_type())


Car("TATA","NEXON")

print(my_car.total_car)
print(Car.total_car)
        
print(Car.general_description())
    
output:
Model X
Electric charge
Petrol or Diesel
3
3
Cars are means of transport

=== Code Execution Successful ===

Q. Use a property decorator in a Car class to make the model attribute read only.
PROPERTY DECORATOR
first we have to make variable as private.
then we have to call that private variable inside the same name function.
apply @property decorator on that function to access it like a variable.
class Car:
    total_car = 0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        # self.total_car += 1   #we can use self as well
        Car.total_car += 1  #class variable
        
    def my_func(self):
        print(f'my car is of {self.__brand} and model is {self.__model}')
        
    def get_brand(self):        #getter method
        return self.__brand + ' !!'
       
    def fuel_type(self):        #polymorphism
        return 'Petrol or Diesel'
        
    @staticmethod                   #decorator
    def general_description():      #static method
        return 'Cars are means of transport'
        
    @property           #property decorator used to make read only variable
    def model(self):
        return self.__model
       
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand=brand
        # self.model=model
        super().__init__(brand,model)   #calling __init__ thats why no need of self
        self.battery_size = battery_size
        
    def fuel_type(self):            #polymorphism
        return 'Electric charge'
        
        
my_electric_car = ElectricCar('Tesla','Model X','85kWh')
print(my_electric_car.model)
print(my_electric_car.fuel_type())


my_car = Car("TATA","SIERA")
# my_car.model = 'City'     #it will throw error bc we have set read only variable with @property decorator
print(my_car.fuel_type())

Car("TATA","NEXON")

print(my_car.total_car)
print(Car.total_car)
print(Car.general_description())
print(my_car.model)     #accessing the model function like a variable bc of @property decorator. used to make variable read only

output:
Model X
Electric charge
Petrol or Diesel
3
3
Cars are means of transport
SIERA

=== Code Execution Successful ===

Q. Demonstrate the use of isinstance() to check if an object is an instance of Car and ElectricCar.  
Class Inheritance and isinstance() function.
class Car:
    total_car = 0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        # self.total_car += 1   #we can use self as well
        Car.total_car += 1  #class variable
        
    def my_func(self):
        print(f'my car is of {self.__brand} and model is {self.__model}')
        
    def get_brand(self):        #getter method
        return self.__brand + ' !!'
       
    def fuel_type(self):        #polymorphism
        return 'Petrol or Diesel'
        
    @staticmethod                   #decorator
    def general_description():      #static method
        return 'Cars are means of transport'
        
    @property           #property decorator used to make read only variable
    def model(self):
        return self.__model
       
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand=brand
        # self.model=model
        super().__init__(brand,model)   #calling __init__ thats why no need of self
        self.battery_size = battery_size
        
    def fuel_type(self):            #polymorphism
        return 'Electric charge'
        

my_car = Car("TATA","SIERA")

my_electric_car = ElectricCar('Tesla','Model X','85kWh')
print(my_electric_car.model)
print(my_electric_car.fuel_type())

print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))
print(isinstance(my_electric_car, ElectricCar))
print(isinstance(my_electric_car, Car))

output:
Model X
Electric charge
True
False
True
True

=== Code Execution Successful ===

Q. Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
MULTIPLE INHERITANCE
class Car:
    total_car = 0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        # self.total_car += 1   #we can use self as well
        Car.total_car += 1  #class variable
        
    def my_func(self):
        print(f'my car is of {self.__brand} and model is {self.__model}')
        
    def get_brand(self):        #getter method
        return self.__brand + ' !!'
       
    def fuel_type(self):        #polymorphism
        return 'Petrol or Diesel'
        
    @staticmethod                   #decorator
    def general_description():      #static method
        return 'Cars are means of transport'
        
    @property           #property decorator used to make read only variable
    def model(self):
        return self.__model
       
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand=brand
        # self.model=model
        super().__init__(brand,model)   #calling __init__ thats why no need of self
        self.battery_size = battery_size
        
    def fuel_type(self):            #polymorphism
        return 'Electric charge'
        

my_car = Car("TATA","SIERA")

my_electric_car = ElectricCar('Tesla','Model X','85kWh')
print(my_electric_car.model)
print(my_electric_car.fuel_type())

print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))
print(isinstance(my_electric_car, ElectricCar))
print(isinstance(my_electric_car, Car))


class Battery:
    def battery_info(self):
        return 'this is battery class'

class Engine:
    def engine_info(self):
        return 'this is engine class'

class ElectricCarTwo(Battery,Engine,Car):
    pass


car1 = ElectricCarTwo('Tesla','Model S')
print(car1.battery_info())
print(car1.engine_info())

output:
Model X
Electric charge
True
False
True
True
this is battery class
this is engine class

=== Code Execution Successful ===
    















