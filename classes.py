# Este arquivo contém exemplos básicos de criação de classes, incluindo a criação 
# de variáveis de classe e métodos, bem como o uso de herança e polimorfismo.

class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
  def bark(self):
    print("Woof!")

class GermanShepherd(Dog):
  def run(self):
    print("Running!")
  def bark(self):
    print("Wau Wau!")

dog1 = Dog("Fido", "Golden Retriever")
dog2 = GermanShepherd("Max", "German Shepherd")

dog1.bark() # prints "Woof!"
dog2.bark() # prints "Wau Wau!"
dog2.run() # prints "Running!"
