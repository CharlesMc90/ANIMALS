import unittest
from animal import Animal
from dog import Dog

class TestAnimals(unittest.TestCase):
    def test_animal_creation(self):
        # Create an Animal instance
        animal = Animal("Generic", "Unknown")
        self.assertEqual(animal.name, "Generic")
        self.assertEqual(animal.species, "Unknown")
        self.assertEqual(animal.kingdom, "Animalia")
        self.assertIn(animal, Animal.all_animals)

    def test_animal_speak(self):
        # Test the speak method of Animal
        animal = Animal("Generic", "Unknown")
        self.assertEqual(animal.speak(), "The animal makes a noise.")

    def test_animal_str(self):
        # Test the __str__ method of Animal
        animal = Animal("Generic", "Unknown")
        self.assertEqual(
            str(animal),
            "Kingdom: 'Animalia', Name: 'Generic', Species: 'Unknown'"
        )

    def test_dog_creation(self):
        # Create a Dog instance
        dog = Dog("Buddy", "Canine", "Golden Retriever")
        self.assertEqual(dog.name, "Buddy")
        self.assertEqual(dog.species, "Canine")
        self.assertEqual(dog.breed, "Golden Retriever")
        self.assertEqual(dog.kingdom, "Animalia")
        self.assertIn(dog, Animal.all_animals)

    def test_dog_speak(self):
        # Test the speak method of Dog
        dog = Dog("Buddy", "Canine", "Golden Retriever")
        self.assertEqual(dog.speak(), "The dog barks.")

    def test_dog_str(self):
        # Test the __str__ method of Dog
        dog = Dog("Buddy", "Canine", "Golden Retriever")
        self.assertEqual(
            str(dog),
            "Kingdom: 'Animalia', Name: 'Buddy', Species: 'Canine', Breed: 'Golden Retriever'"
        )

    def test_all_animals(self):
        # Test the class-level all_animals list
        Animal.all_animals = []  # Clear list for fresh test
        animal = Animal("Generic", "Unknown")
        dog = Dog("Buddy", "Canine", "Golden Retriever")
        self.assertEqual(len(Animal.all_animals), 2)
        self.assertIn(animal, Animal.all_animals)
        self.assertIn(dog, Animal.all_animals)

if __name__ == "__main__":
    unittest.main()
