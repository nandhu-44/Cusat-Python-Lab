"""
1. Develop a program to read a four-digit number and find its
   a. Sum of digits
   b. Reverse
   c. Difference between the product of digits at the odd position
and the product of digits at the even position.
"""

# Function to extract digits and return as a list.
def extract_digits(number):
    return [int(i) for i in str(number)]

#  Function to reverse a given integer
def reverse(number):
    reverse_number = 0
    while number > 0:
        remainder = number % 10
        number //= 10
        reverse_number = reverse_number * 10 + remainder
    return reverse_number

# Function to find the difference of products 
def alternative_product(number):
    num = extract_digits(number)
    return (num[0] * num[2]) - (num[1] * num[3])

# Main Program
number = int(input("Enter a four digit number: "))

# Terminating program if the number is not 4 digit number
if len(extract_digits(number)) != 4 :
    print("Please provide a four digit number!")
    exit()

yes = True
content = """
______ Main Menu ______
1. Sum of digits
2. Reverse
3. Difference between the product of digits
4. Exit
"""
while yes:
    print(content)
    choice = int(input("Enter your choice: "))
    print("__________________________________________")
    if choice == 1:
        # Program to find the sum of digits
        sum = 0
        for i in extract_digits(number):
            sum += i
        print(f"The sum of the digits of {number} is {sum}")
    elif choice == 2:
        # Program to reverse the number
        reverse_of_number = reverse(number)
        print(f"The reverse of {number} is {reverse_of_number}")
    elif choice == 3:
        # Program to find the difference of products
        difference_of_products = alternative_product(number)
        print(f"The difference of the products is {difference_of_products}")
    elif choice == 4:
        print("Thank you for using the program!")
        yes = False
    else:
        print("Please enter a valid choice!")
    print("__________________________________________")