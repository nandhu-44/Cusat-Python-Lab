"""
5. Write a program to create a parent class, 3DShapes, with methods
printVolume() and printArea(), which prints the Volume and Area,
respectively. Create classes Cylinder and Sphere by inheriting
3DShapes class. Using these child classes, calculate and print the
volume and area of a cylinder and sphere.
"""
# Base class
class __3DShapes__:
    def print_area(self,shape):
        print(f"Area of the {shape} is: {self.area} ")

    def print_volume(self,shape):
        print(f"Volume of the {shape} is: {self.volume} ")

# Inherited class 1 for cylinder
class Cylinder(__3DShapes__):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.area = self.calculate_area()
        self.volume = self.calculate_volume()

    def calculate_area(self):
        return round((2 * 3.14 * self.radius * self.height) + (2 * 3.14 * self.radius ** 2), 2)
    
    def calculate_volume(self):
        return round(3.14 * (self.radius ** 2) * self.height, 2)

# Inherited class 2 for sphere
class Sphere(__3DShapes__):
    def __init__(self, radius):
        self.radius = radius
        self.area = self.calculate_area()
        self.volume = self.calculate_volume()

    def calculate_area(self):
        return round(4 * 3.14 * (self.radius ** 2), 2)
    
    def calculate_volume(self):
        return round((4/3) * 3.14 * (self.radius ** 3), 2)
    
# Main program
print()
# Taking input from the user for radius and height of the cylinder
print("-----Cylinder-----")
radius = float(input("Enter radius of the cylinder: "))
height = float(input("Enter height of the cylinder: "))
cylinder = Cylinder(radius, height)
print()
# Taking input from the user for radius of the sphere
print("-----Sphere-----")
radius = float(input("Enter radius of the sphere: "))
sphere = Sphere(radius)

contents = """
----------------------------------------------------------------------------------------------------
-----Main Menu-----
1. Print area and volume of the cylinder
2. Print area and volume of the sphere
3. Exit
"""

while True:
    print(contents)
    choice = int(input("Enter your choice: "))
    print()
    print("----------------------------------------------------------------------------------------------------")
    print()
    if choice == 1:
        cylinder.print_area("cylinder")
        cylinder.print_volume("cylinder")
    elif choice == 2:
        sphere.print_area("sphere")
        sphere.print_volume("sphere")
    elif choice == 3:
        print("Thank you for using the program.")
        break
    else:
        print("Please provide a valid choice!")
print()