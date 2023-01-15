"""
2. Develop a program to read the three sides of two triangles and calculate the area of both.
Define a function to read the three sides and call it.
Also, define a function to calculate the area. 
Print the total area enclosed by both triangles and each triangle's contribution (%) towards it.
"""

# Importing math library to use the square root function
import math

# Function Declarations
# Function to take user input of the three sides
def read_sides(triangle_number):
    print(f">> Triangle {triangle_number} <<")
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))
    return side1,side2,side3

# Function to calculate the area of a triangle
def find_area(side1,side2,side3):
    semiperimeter = (side1 + side2 + side3)/2
    area = math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))
    return area

# Function to calculate the total area of two triangles
def find_total_area(area1,area2):
    total_area = area1 + area2
    return total_area

# Function to calculate the percentage contribution of each triangle
def percentage_contribution(area1,area2):
    total_area = find_total_area(area1,area2)
    contribution1 = round(area1/total_area,2) * 100
    contribution2 = 100 - contribution1
    return contribution1,contribution2

# Function to check if the triangle is valid
def is_valid_triangle(side1, side2, side3):
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
        return True
    else:
        return False


# Main Program
# Triangle 1
print()
side_a1,side_b1,side_c1 = read_sides(1)
if(is_valid_triangle(side_a1,side_b1,side_c1) == False):
    print("Please provide the lengths of a triangle that is valid!")
    print()
    exit()
area_1 = find_area(side_a1,side_b1,side_c1)

# Trinagle 2
print()
side_a2,side_b2,side_c2 = read_sides(2)
if(is_valid_triangle(side_a2,side_b2,side_c2) == False):
    print("Please provide the lengths of a triangle that is valid!")
    print()
    exit()
area_2 = find_area(side_a2,side_b2,side_c2)


yes = True
content = """
______ Main Menu ______
1. Find the area of each triangle
2. Find the total area of both triangles
3. Find the percentage contribution of each triangle
4. Exit
"""
while yes:
    print(content)
    choice = int(input("Enter your choice: "))
    print()
    print("______________________________________________________________________________________________")
    print()
    if choice == 1:
        # Printing the areas of the triangles
        print(f"The area of the triangle 1 is {round(area_1,2)} sq. units")
        print(f"The area of the triangle 2 is {round(area_2,2)} sq. units")
    elif choice == 2:
        # Finding the total area of the two triangles
        total_area_of_both = find_total_area(area_1,area_2)
        print(f"The total area of the two triangles is {round(total_area_of_both,2)} sq. units")
    elif choice == 3:
        # Finding the percentage contribution of each triangle
        percentage_contribution1,percentage_contribution2 = percentage_contribution(area_1,area_2)
        print(f"The percentage contribution of triangle 1 is {percentage_contribution1}%")
        print(f"The percentage contribution of triangle 2 is {percentage_contribution2}%")
    elif choice == 4:
        print("Thank you for using the program!")
        yes = False
    else:
        print("Please enter a valid choice!")
    print("______________________________________________________________________________________________")
    print()