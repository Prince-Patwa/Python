# Add a static method to the Car class that returns a general description of car.

class Car:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def genral_description(name):
        return f"{name} is very good car."

my_car = Car("Tata")
print(my_car.genral_description("Nexion"))
print(Car.genral_description("Safari"))