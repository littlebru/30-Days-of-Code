class Person:
  def __init__(self, initialAge):
    self.age = initialAge
    
    if self.age < 0:
      print('Age is not valid, setting age to 0.')
      self.age = 0
    
  def amIOld(self):
    if self.age < 13:
      print('You are young.')
    elif 13 <= self.age < 18:
      print('You are a teenager.')
    elif self.age >= 18:
      print('You are old.')
      
  def yearPasses(self):
    x = self.age
    self.age += 1
    return x


time = int(input())
years = 3

for i in range(0,time):
  age = int(input())      
  p = Person(age)
  p.amIOld()
  
  for j in range(0,years):
    p.yearPasses()

  p.amIOld()
  print("")
    
