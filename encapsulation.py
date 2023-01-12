# Este arquivo contém exemplos de encapsulamento e uso de métodos getter e setter.

class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed
        
    def get_name(self):
        return self._name
    
    def set_name(self,name):
        self._name = name
        
    def get_breed(self):
        return self._breed
    
    def set_breed(self,breed):
        self._breed = breed
        
dog = Dog("Fido", "Golden Retriever")
print(dog.get_name()) # prints "Fido"
dog.set_name("Max")
print(dog.get_name()) # prints "Max"
