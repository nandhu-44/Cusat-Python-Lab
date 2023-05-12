"""
4. Write a program to create a class Box with data members length,
breadth, height, area, and volume. Provider constructor that enables
initialization with one parameter (for cube), two parameters (for
square prism) three parameters (rectangular prism). Also, provide
functions to calculate area and volume.
Create a list of N boxes with random measurements and print the
details of the box with maximum volume: area ratio
"""

# Importing random module to generate random numbers
from random import randint,shuffle

# Defining the Box class
class Box:
    def __init__(self, length, width=None, height=None):
        self.length = length
        # One parameter is passed, so it is a cube
        if width is None and height is None:
            self.width = length
            self.height = length
        # Two parameters are passed, so it is a square prism
        elif width is not None and height is None:
            self.width = width
            self.height = length
        # Three parameters are passed, so it is a rectangular prism
        else:
            self.width = width
            self.height = height
        self.area = self.calculate_area()
        self.volume = self.calculate_volume()
        
    # Function to calculate the surface area of the box
    def calculate_area(self):
        return 2 * (self.length * self.width + 
        self.length * self.height + self.width * self.height)
    
    # Function to calculate the volume of the box
    def calculate_volume(self):
        return self.length * self.width * self.height
    
    # Function to calculate the volume:area ratio of the box
    def get_volume_area_ratio(self):
        return self.volume / self.area
    
    # Overloading the __str__ method to print the box
    def __str__(self):
        return f"Box({self.length}, {self.width}, {self.height})"


# Generating a list of 4 rectangular prisms, 3 square prisms and 3 cubes
list_rec_prisms = [ Box(randint(1, 10), 
            randint(1, 10), randint(1, 10)) for i in range(4)]
list_square_prisms = [ Box(randint(1, 10),
                              randint(1, 10)) for i in range(3)]
list_of_cubes = [ Box(randint(1, 10)) for i in range(3)]
# Combining all the lists into a single list of 10 boxes of random dimensions
list_of_boxes = list_rec_prisms + list_square_prisms + list_of_cubes

# Shuffling the list to randomize the order of the boxes
shuffle(list_of_boxes)
content = """
-----------------------------------------------------------
-----Main Menu-----
1. Show all the boxes
2. Get maximum volume:area ratio
3. Exit"""
print(content)
while True:
    print("\n-----------------------------------------------------------\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        for box in list_of_boxes:
            print(f"Box {list_of_boxes.index(box) + 1}: {box}")
    elif choice == 2:
        box_ratio = [ box.get_volume_area_ratio() for box in list_of_boxes ]
        print(f"Box {box_ratio.index(max(box_ratio))+ 1}",
        f"has the maximum volume:area ratio of {round(max(box_ratio),3)}")
    elif choice == 3:
        print("Thank you for using the program.")
        break
    else:
        print("Please enter a valid choice!")