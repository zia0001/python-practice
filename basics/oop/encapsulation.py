class Car:

  def __init__(self, brand, model):
    self.__brand = brand
    self.__model = model

  def get_brand(self):
      return self.__brand  
  
  def get_model(self):
    return self.__model
    
    

# c1= Car('pijaro', 2021)
# print( c1.brand,':' ,c1.model)

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size
    
c3 = ElectricCar('Toyota',2025,'24F')
print(c3.get_brand())
print(c3.get_model())
 