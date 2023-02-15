"""
4. Write a program to create a class Box with data members length,
breadth, height, area, and volume. Provider constructor that enables
initialization with one parameter (for cube), two parameters (for
square prism) three parameters (rectangular prism). Also, provide
functions to calculate area and volume.
Create a list of N boxes with random measurements and print the
details of the box with maximum volume: area ratio*
"""

# Importing random module to generate random numbers
import random

# Defining the Box class
class Box:
    # Constructor with 1 argument for cube 
    def __init__(self, arg1):
        self.length = arg1
        self.width = arg1
        self.height = arg1
    
    # Constructor with 2 arguments for square prism
    def __init__(self, arg1, arg2) :
        self.length = arg1
        self.width = arg1
        self.height = arg2
    
    # Constructor with 3 arguments for rectangular prism
    def __init__(self, arg1, arg2, arg3) :
        self.length = arg1
        self.width = arg2
        self.height = arg3
        
    # Function to calculate the surface area of the box
    def calculate_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
    
    # Function to calculate the volume of the box
    def calculate_volume(self):
        return self.length * self.width * self.height
    
    # Function to calculate the volume:area ratio of the box
    def get_volume_area_ratio(self):
        return self.calculate_volume() / self.calculate_area()
    
    # Overloading the __str__ method to print the box
    def __str__(self):
        return f"Box({self.length}, {self.width}, {self.height})"


# Main Program 
# Creating a list of 10 boxes with random dimensions
list_of_boxes = [ Box(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)) for i in range(10) ]

yes = True
content = """
____Main Menu____
1. Show all the boxes
2. Get maximum volume:area ratio
3. Exit
"""
while yes:
    print(content)
    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        for box in list_of_boxes:
            print(f"Box {list_of_boxes.index(box) + 1}: {box}")
    elif choice == 2:
        box_ratio = [ box.get_volume_area_ratio() for box in list_of_boxes ]
        print(f"Box {box_ratio.index(max(box_ratio))+ 1} has the maximum volume:area ratio of {round(max(box_ratio),3)}")
    elif choice == 3:
        print("Thank you for using the program!")
        yes = False
    else:
        print("Please enter a valid choice!")
    print()