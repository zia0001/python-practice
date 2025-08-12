class Car:

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def fuel_type(self):
    return "Petrol or Diesel or CNG"
    

c1= Car('pijaro', 2021)


class ElectricCar(Car):
  
  def fuel_type(self):     #common method but different usage
    return "Electric charge"
  
Ecar = ElectricCar('Tesla', 2025)
print(f"{Ecar.brand} {Ecar.model} {Ecar.fuel_type()}")

print(Ecar)

