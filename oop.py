class Dog:
    # Class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is",self.name)

# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a",Dog.attr1)  # Accessing class attribute directly
print("Tommy is also a",Dog.attr1)  # Accessing class attribute directly

# Accessing instance attributes
print("My name is {}".format(Rodger.name))  # Accessing instance attribute directly
print("My name is {}".format(Tommy.name))  # Accessing instance attribute directly

Rodger.speak()
Tommy.speak()