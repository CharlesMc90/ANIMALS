class Animal:
    # Class-level attribute to store all Animal instances
    all_animals = []

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.kingdom = "Animalia"  # All animals belong to the Animalia kingdom
        # Add the instance to the class-level list
        Animal.all_animals.append(self)

    def speak(self):
        return "The animal makes a noise."

    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"
