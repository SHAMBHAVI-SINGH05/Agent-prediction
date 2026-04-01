class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says wolf! & is {self.age} years old")

# Using the class (outside of the class and method)
my_dog = Dog("Buddy",4)
my_dog.bark()
print("The age is",my_dog.age)
print("The name is",my_dog.name)

