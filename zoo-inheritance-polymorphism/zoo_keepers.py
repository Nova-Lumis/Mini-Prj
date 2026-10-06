# Animal Class as parent
class Animal:
    """Parent class for animal"""
    # Construction instance attr
    def __init__(self, name, energy = 10):
        self.name = name
        self.energy = energy
    
    # Methods
    def speak(self):
        raise NotImplementedError("Children must provide their own")
    
    # Eat increase energy
    def eat(self, food_energy):
        self.energy += food_energy
    
    # Display message
    def describe(self):
        return (f"'{self.name}' has {self.energy} energy")

class Dog(Animal):
    """Children class describing a Dog from Animal Parent class"""
    # Speaking
    def speak(self):
        return (f"Woof, woof! My name is '{self.name}' and I am a dog.")
    
    # Describe a message
    def describe(self):
        return (f"{super().describe()}, loves walk")


class Cat(Animal):
    """Children class describing a Cat from Animal Parent class"""
    # Speaking
    def speak(self):
        return (f"Meowwww. My name is '{self.name}' and I am a cat.")

    # Describe a message
    def describe(self):
        return (f"{super().describe()}, loves sleep and eat")


class Bird(Animal):
    """Children class describing a Bird from Animal Parent class"""
    # Constructor
    def __init__(self, name, energy=10, can_fly = True):
        super().__init__(name, energy)
        self.can_fly = can_fly
    
    # Speaking
    def speak(self):
        return (f"Chirp, Chirp. My name is '{self.name}'. I am a bird.")

class Fish(Animal):
    """Children class describing a Fish from Animal Parent class"""
    # Speaking
    def speak(self):
        return (f"SPLASHHH!!! My name is '{self.name}'. I am a mighty fish")
    
    # Skills
    def splashing(self):
        return (f"{self.name} is splashing water everywhere!!!")

# Return the animal speaking method
def make_all_speak(animals):
    for animal in animals:
        print(f"{animal.speak()}")
        print(f"{animal.describe()}\n")


# Main program
try:
    dog_1 = Dog("dog", 10)
    cat_1 = Cat("Jack", 30)
    bird_1 = Bird("Fan", 15, True)
    cat_1.eat(20)
    fish_1 = Fish("Magikarp")
    make_all_speak([dog_1, cat_1, bird_1, fish_1])
    print(fish_1.splashing())

except NotImplementedError as e:
    print("Error: ", e)

