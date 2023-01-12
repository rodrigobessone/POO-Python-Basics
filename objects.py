# Este arquivo contém exemplos de criação de objetos a partir de classes e 
# uso de métodos e variáveis de objeto.

class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
  def bark(self):
    print("Woof!")

dog1 = Dog("Fido", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(dog1.name) # prints "Fido"
print(dog2.breed) # prints "German Shepherd"
dog2.bark() # prints "Woof!"
