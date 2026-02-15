class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        def get_brand(self):
            return self.brand + "!"
    #def full_name(self):
        #return f"{self._brand} {self.model}"# formatted string
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def genetral_discription():
        return " Cars are vehicle"
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size # it's extra part
    def fuel_type(self):
        return "electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85 kWh")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))

class Battery:
    # pass is a null statement — it does nothing
    def batteyinfo(self):
        return "This is battery"


class Engine:
    def engineinfo(self):
        return "This is engine"

class EelctricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = EelctricCarTwo("Tesla", "Model S")
# Multiple inheritance
print(my_new_tesla.engineinfo())
print(my_new_tesla.batteyinfo())
# print(my_tesla.model)
# print(my_tesla.full_name())
#print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
#  my_car.model = "City"
#  Car("Tata", "Nexon")
# print(my_car.model)
#safari3 = Car("Tata","nexon")
#print(Car.total_car)

# the below two lines are same
# print(safari.genetral_discription())
# print(Car.genetral_discription())

# my_car = Car("Toyota", "Corolla")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())# bcz fullname is not a attribute , it's a function


# my_newcar = Car("Ferrari","Q7")
# print(my_newcar.brand)
# print(my_newcar.model)


