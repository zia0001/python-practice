class Car:
  total_cars = 0
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    Car.total_cars += 1
  def fuel_type(self):
    return "Petrol or Diesel or CNG"
    

#c1= Car('pijaro', 2021)


class ElectricCar(Car):
  
  def fuel_type(self):     #common method but different usage
    return "Electric charge"
  
Ecar = ElectricCar('TATA', 2025)
print(f"{Ecar.brand} {Ecar.model} {Ecar.fuel_type()}")

print(Car.total_cars)

