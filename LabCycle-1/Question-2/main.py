"""
2. Develop a program to read the three sides of two triangles and calculate the area of both.
Define a function to read the three sides and call it.
Also, define a function to calculate the area. 
Print the total area enclosed by both triangles and each triangle's contribution (%) towards it.
"""

# Function to take user input of the three sides
def read_sides(triangle_number):
    print(f">> Triangle {triangle_number} <<")
    return [int(i) for i in input("Enter the three sides : ").split()]

# Function to calculate the area of a triangle
def find_area(s1,s2,s3):
    s = (s1 + s2 + s3)/2
    return (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
    
# Function to calculate the total area of two triangles
def find_total_area(area1,area2):
    return area1 + area2

# Function to calculate the percentage contribution of each triangle
def percentage_contribution(area1,area2):
    total_area = find_total_area(area1,area2)
    contribution1 = round(area1/total_area,2) * 100
    contribution2 = 100 - contribution1
    return contribution1,contribution2

# Function to check if the triangle is valid
def is_valid_triangle(s1, s2, s3):
    return (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)

# Triangle 1
side_a1,side_b1,side_c1 = read_sides(1)
if(not is_valid_triangle(side_a1,side_b1,side_c1)):
    print("Please provide valid sides!")
    exit()
area_1 = find_area(side_a1,side_b1,side_c1)
# Trinagle 2
side_a2,side_b2,side_c2 = read_sides(2)
if(not is_valid_triangle(side_a2,side_b2,side_c2)):
    print("Please provide valid sides!")
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
print(content)
while yes:
    choice = int(input("Enter your choice: "))
    print("-----------------------------------------------------")
    if choice == 1:
        print(f"The area of the triangle 1 is {round(area_1,2)} ")
        print(f"The area of the triangle 2 is {round(area_2,2)} ")
    elif choice == 2:
        total_area = find_total_area(area_1,area_2)
        print(f"The total area is {round(total_area,2)} ")
    elif choice == 3:
        pc1,pc2 = percentage_contribution(area_1,area_2)
        print(f"The % contribution of triangle 1 is {pc1}%")
        print(f"The % contribution of triangle 2 is {pc2}%")
    elif choice == 4:
        print("Thank you for using the program!")
        yes = False
    else:
        print("Please enter a valid choice!")
    print("-----------------------------------------------------")