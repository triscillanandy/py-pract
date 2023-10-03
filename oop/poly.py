# Define a base class called Bird
#shows how subclasses can overridSe methods
# defined in their parent class to 
#provide specific behavior while still inheriting 
#other methods from the parent class.
class Bird:
    def intro(self):
        print("There are many types of birds")
        
    def flight(self):
        print("Most birds can fly, but some can't")

# Define a derived class called Sparrow, which inherits from Bird
class Sparrow(Bird):
    # Override the flight method for Sparrows
    def flight(self):
        print("Sparrows can fly")

# Define another derived class called Ostrich, which also inherits from Bird
class Ostrich(Bird):
    # Override the flight method for Ostriches
    def flight(self):
        print("Ostriches cannot fly")

# Create an instance of the Sparrow class
sparrow_ob = Sparrow()
# Call the intro method from the Bird class
sparrow_ob.intro()
# Call the flight method specific to Sparrows
sparrow_ob.flight()

# Create an instance of the Ostrich class
ostrich_ob = Ostrich()
# Call the intro method from the Bird class
ostrich_ob.intro()
# Call the flight method specific to Ostriches
ostrich_ob.flight()
