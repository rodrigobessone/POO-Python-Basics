# Este arquivo contém exemplos de abstração e 
# uso de classes abstratas e interfaces.

from abc import ABC, abstractmethod

class Animals(ABC):
    def __init__(self,name):
        self.name = name
        
    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animals):
    def speak(self):
        return "Woof!"
    
class Cat(Animals):
    def speak(self):
        return "Meow!"

dog = Dog("dog")
print(dog.speak()) # prints "Woof!"

cat = Cat("cat")
print(cat.speak()) # prints "Meow!"
