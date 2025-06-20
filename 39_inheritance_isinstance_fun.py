# Demonstrate the use of isinstance() to check if my_tesla is an instance of Var and ElectricCar.

class Car:
    def __init__(self, brand, model):
            self.brand = brand
            self.model = model
    def full_name(self):
          print(f"Car brand is - {self.brand} and car model name is - {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
            super().__init__(brand, model)  
            self.battery_size = battery_size
          

my_tesla = ElectricCar("Tata", "Safari", "80kWh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))