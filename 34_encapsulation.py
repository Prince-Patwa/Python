# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
            self.__brand = brand
            self.model = model
    def get_brand(self):
          return self.__brand
    def full_name(self):
          print(f"Car brand is - {self.__brand} and car model name is - {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
            super().__init__(brand, model)  
            self.battery_size = battery_size

my_car = ElectricCar("Tata", "Safari", "80kWh")
# my_car.full_name()
print(my_car.get_brand())