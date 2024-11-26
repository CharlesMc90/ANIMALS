from animal import Animal
from dog import Dog

def main():
    # Create and test an Animal instance
    generic_animal = Animal("Generic", "Unknown")
    print(generic_animal)  # Test __str__ method
    print(generic_animal.speak())  # Test speak method

    # Create and test a Dog instance
    buddy = Dog("Buddy", "Canine", "Golden Retriever")
    print(buddy)  # Test overridden __str__ method
    print(buddy.speak())  # Test overridden speak method

    # Test the class-level list
    print("\nAll Animals:")
    for animal in Animal.all_animals:
        print(animal)

if __name__ == "__main__":
    main()
