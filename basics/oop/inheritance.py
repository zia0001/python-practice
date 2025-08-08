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