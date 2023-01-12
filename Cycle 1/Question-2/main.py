# Importing math library to use the square root function
import math

# Function Declarations
# Function to take user input of the three sides
def read_sides():
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))
    return side1,side2,side3


def find_area(side1,side2,side3):
    semiperimeter = (side1 + side2 + side3)/2
    area = math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))
    return area


def find_total_area(area1,area2):
    total_area = area1 + area2
    return total_area


def percentage_contribution(area1,area2):
    total_area = find_total_area(area1,area2)
    contribution1 = round(area1/total_area,2) * 100
    contribution2 = 100 - contribution1
    return contribution1,contribution2


def is_valid_triangle(side1, side2, side3):
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
        return True
    else:
        return False



print("Triangle 1")
side_a1,side_b1,side_c1 = read_sides()
if(is_valid_triangle(side_a1,side_b1,side_c1) == False):
    print("Please provide the lengths of a triangle that ia valid!")
    exit()
area_1 = find_area(side_a1,side_b1,side_c1)
print(f"The area of the triangle is {area_1}")


print("Triangle 2")
side_a2,side_b2,side_c2 = read_sides()
if(is_valid_triangle(side_a2,side_b2,side_c2) == False):
    print("Please provide the lengths of a triangle that ia valid!")
    exit()
area_2 = find_area(side_a2,side_b2,side_c2)
print(f"The area of the triangle is {area_2}")


total_area_of_both = find_total_area(area_1,area_2)
print(f"The total area of the two triangles is {total_area_of_both}")


percentage_contribution1,percentage_contribution2 = percentage_contribution(area_1,area_2)
print(f"The percentage contribution of triangle 1 is {percentage_contribution1}%")
print(f"The percentage contribution of triangle 2 is {percentage_contribution2}%")

