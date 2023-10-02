#Polymorphism simply means having many form

class Bird:
    def intro(self):
        print("there are many birds types")
    def flight (self):
        print("Most can fly other cant fly")

class sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")
class ostrich(Bird):
    def flight(self):
        print("Ostrich can not fly")


sparrow_ob = sparrow()
sparrow_ob.intro()
sparrow_ob.flight()

ostrich_ob = ostrich()
ostrich_ob.intro()
ostrich_ob.flight()