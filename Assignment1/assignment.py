from abc import ABC , abstractmethod
import math

class Student:
    def __init__(self , name , age , grade):
        #now down comes the attributes 
        self.name = name 
        self.__age = age # so __ means private varibables and it cannot be accesssed directly outside the class
        self.grade = grade

    # encapsulaiton pov these are getter and setter 
    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
        
    # to display student ingormation we make display method
    def display_info(self):
        print(f"Name: {self.name} , Age: {self.__age}, Grade: {self.grade}")


class HighSchoolStudents(Student):
    def __init__(self , name , age , grade , grade_level):
        super().__init__(name , age, grade) # this super is like in java calls the parent class constructor
        self.grade_level = grade_level

    def display_info(self):
        print(
            f"Name: {self.name}, Age: {self.get_age()}, "
            f"Grade: {self.grade}, Grade Level: {self.grade_level}"
        )

#poly
def print_student_info(obj):
    obj.display_info()


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius
    

class rectangle(Shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    

p = Student("Sahil" , "21" , "B")
c= HighSchoolStudents("Mayank" , "22", "A" ,"ECE-4th-Year")

print_student_info(p)
print_student_info(c)

circle = Circle(5)
rect_obj = rectangle(4, 6)

print("Circle Area:", circle.calculate_area())
print("Rectangle Area:", rect_obj.calculate_area())
