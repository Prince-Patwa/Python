# Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
            self.brand = brand
            self.model = model

    def car(self, brand, model):
          print(f"Car brand is {brand} and car name is {model}")

my_car = Car("Tata", "Safari")

my_car.car("Tata", "Safari")