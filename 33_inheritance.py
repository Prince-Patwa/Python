# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

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
    # def battery_size(self):
    #       print(f"Car brand is - {self.brand}, car model name is - {self.model} and battery size is : {self.battery_size}")
          

my_car = ElectricCar("Tata", "Safari", "80kWh")
my_car.full_name()
print(my_car.battery_size)
# my_car.battery_size()