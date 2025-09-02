#Answer 1
# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Encapsulation: private attribute

    def call(self, number):
        print(f"{self.model} is calling {number} 📞")

    def get_price(self):
        return self.__price

# Inheritance: GamingPhone inherits from Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, gpu_power):
        super().__init__(brand, model, price)
        self.gpu_power = gpu_power

    def play_game(self, game):
        print(f"Playing {game} on {self.model} with GPU power {self.gpu_power} 🎮")

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 1200)
phone2 = GamingPhone("Asus", "ROG Phone 7", 1000, "High")

phone1.call("123-456-7890")
phone2.call("987-654-3210")
phone2.play_game("Call of Duty")

print("Price of phone2:", phone2.get_price())

#Answer 2
# Base class: Animal
class Animal:
    def move(self):
        pass  # Generic method

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

# Polymorphism in action
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    animal.move()  # Each class defines move() differently
