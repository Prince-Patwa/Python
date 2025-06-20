# Demonstrate polymorphism by defining a method fule_type in both Car and ElectricCar classes, but with different bahaviors.

class Car:
    def __init__(self, brand):
            self.brand = brand
    def fule_type(self):
          return "Fule type is : Petrol or Diesel"

class ElectricCar():
    def __init__(self, brand):
                self.brand = brand
    def fule_type(self):
           return "Fule type is : Electric charge"

my_ecar = ElectricCar("Tesla")
print(my_ecar.fule_type()) 

my_car = Car("Tata")
print(my_car.fule_type())