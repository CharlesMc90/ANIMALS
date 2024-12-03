from animal import Animal
from dog import Dog

# Create and test an Animal instance
animal1 = Animal("Generic", "Unknown")
print(animal1)                # Test __str__
print(animal1.speak())        # Test speak()

# Create and test a Dog instance
dog1 = Dog("Buddy", "Canine", "Golden Retriever")
print(dog1)                   # Test overridden __str__
print(dog1.speak())           # Test overridden speak()

# Test the class-level list
print("All Animals:")
for animal in Animal.all_animals:
    print(animal)
