class Classroom:
    classlist = {}  # Class-level variable to store class lists
    
    def __init__(self, room_number, teacher, students=None):
        self.room_number = room_number
        self.teacher = teacher
        self.students = students if students else []

    def add_student(self, student_name):
        self.students.append(student_name)

    def remove_student(self, name):
        if name in self.students:
            self.students.remove(name)
        else:
            print("That name does not exist")

    def matches_age(self, age):
        new_age = int(input("Enter age as a number: "))
        if new_age == age:
            self.students.append(new_age)

    def get_classlist(self):
        print("Room Number:", self.room_number)
        print("Teacher:", self.teacher)
        print("Students:")
        for student in self.students:
            print(student)


# Example usage:
# Create a Classroom instance
classroom = Classroom("101", "Mr. Smith", ["Alice", "Bob", "Charlie"])

# Add a student to the class
classroom.add_student("David")

# Remove a student from the class
classroom.remove_student("Bob")

# Print the classlist
classroom.get_classlist()
