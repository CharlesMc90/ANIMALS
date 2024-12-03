class Animal:
    all_animals = []  # Class-level attribute to store all instances

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.kingdom = "Animalia"
        Animal.all_animals.append(self)

    def speak(self):
        return "The animal makes a noise."

    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"
