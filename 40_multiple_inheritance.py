# Create two classes Battery and Engine, and let the ElectricCar class inherit form both, demonstrating multiple inheritance.

class Battery:
    # def __init__(self, battery):
    #     self.battery = battery
    def battery(self):
        return "This is electric car."

class Engine:
    # def __init__(self, fule):
    #     self.fule = fule
    def engine(self):
        return "This is fule car."

class ElectricCar(Battery, Engine):
    # def __init__(self, battery, fule):
    #     self.battery = battery
    #     self.fule = fule
    pass

my_car = ElectricCar()
print(my_car.battery())
print(my_car.engine())