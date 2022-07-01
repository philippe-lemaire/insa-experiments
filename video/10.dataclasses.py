from dataclasses import dataclass


@dataclass
class Student:
    """Class for keeping track of an item in inventory."""
    first_name: str
    last_name: str
    student_id: int

    def greet(self):
        return f"Hello I am {self.first_name} {self.last_name}."


student = Student('Philippe', 'Lemaire', 129812)

print(student.greet())
