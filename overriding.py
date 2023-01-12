# Este arquivo contém exemplos de sobrecarga de métodos e variáveis de classe.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print("Woof!")
        
class GoldenRetriever(Dog):
    def bark(self):
        print("Woof, woof!")
        
dog = Dog("Fido", "Golden Retriever")
dog.bark() # prints "Woof!"

goldenRetriever = GoldenRetriever("Max","Golden Retriever")
goldenRetriever.bark() # prints "Woof, woof!"
