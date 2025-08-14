class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    

  def full_name(self):
    return(f"{self.brand} : {self.model}")


  # def __str__(self):
  #   return self.full_name()

c1 = Car("KIA", 2024)
c2 = Car("Mehran", 2025)


print(c1.full_name())
print(c2.full_name())

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

  def full_name(self):
    return f"{self.brand} : {self.model} : Battery {self.battery_size}"
  

  # def __str__(self):
  #   return f"{self.full_name()} with battery {self.battery_size}"



c3 = ElectricCar('Toyota',2025,'24F')
print(c3.full_name())
