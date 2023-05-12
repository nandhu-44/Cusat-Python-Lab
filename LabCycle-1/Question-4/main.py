"""
4. Develop a program to perform the following task:
a. Define a function to check whether a number is happy or not.
b. Define a function to print all happy numbers within a range.
c. Define a function to print first N happy numbers.Ahappy numberis a number defined by the following process:
  • Starting with any positive integer, replace the number withthe sum of the squares of its digits.
  • Repeat the process until the number equals 1 (where it will stay), or itloops endlessly in a cyclewhich does not include 1.
  • Those numbers for which this processends in 1are happy.
Note: if a number is not being happy after 100 iterations, consider it sad.
"""

# Function to check if a number is happy or not
def check_happy_number(number):
    if number < 1:
        return False
    for i in range(100):
        number = sum_of_squares(number)
        if number == 1:
            return True
    return False

# Function to find the sum of squares of digits of a number
def sum_of_squares(number):
    sum = 0
    while number > 0:
        remainder = number % 10
        number //= 10
        sum += remainder ** 2
    return sum

# Function to print all happy numbers in a range
def happy_numbers_in_range(lower_l, upper_l):
    happy_numbers = []
    for i in range(lower_l, upper_l + 1):
        if check_happy_number(i):
            happy_numbers.append(i)
    return happy_numbers

# Function to print first N happy numbers
def first_n_happy_numbers(n):
    happy_numbers = []
    i = 1
    while len(happy_numbers) < n:
        if check_happy_number(i):
            happy_numbers.append(i)
        i += 1
    return happy_numbers

# Function to iterate the list and return a string
def to_string(list):
    string = ""
    for i in list:
        string += f"{i}, "
    return string[:-2]

# Main Program
content = """
______ Main Menu ______
1. Check if a number is happy or not
2. Print all happy numbers in a range
3. Print first N happy numbers
4. Exit"""
yes = True
print(content)
print("-----------------------------------------------------")
while yes:
    choice = int(input("Enter your choice: "))
    print("-----------------------------------------------------")
    if choice == 1:
        number = int(input("Enter a number: "))
        if check_happy_number(number):
            print(f"{number} is a happy number")
        else:
            print(f"{number} is not a happy number")
    elif choice == 2:
        lower_l = int(input("Enter the lower limit: "))
        upper_l = int(input("Enter the upper limit: "))
        happy_numbers = happy_numbers_in_range(lower_l, upper_l)

        if len(happy_numbers) == 0:
            print("There are no happy numbers in the given range!")
        else:
            print(f"Happy numbers in the given range : ", end="")
            print(f"{to_string(happy_numbers)}")
    elif choice == 3:
        n = int(input("Enter the no of terms(happy numbers) to print: "))
        happy_numbers = first_n_happy_numbers(n)
        print(f"The first {n} happy numbers : {to_string(happy_numbers)}")
    elif choice == 4:
        print("Thank you for using the program!")
        yes = False
    else:
        print("Please enter a valid choice!")
    print("-----------------------------------------------------")