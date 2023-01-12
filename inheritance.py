# Este arquivo contém exemplos de herança múltipla e sobrecarga de métodos.

class Animal:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Fish(Animal):
    def speak(self):
        return "...."
    
dog = Dog("dog")
print(dog.speak()) # prints "Woof!"

cat = Cat("cat")
print(cat.speak()) # prints "Meow!"

fish = Fish("fish")
print(fish.speak()) # prints "...."
