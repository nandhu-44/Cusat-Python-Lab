"""
1. Develop a program to read a four-digit number and find its
   a. Sum of digits
   b. Reverse
   c. Difference between the product of digits at the odd position
and the product of digits at the even position.
"""

# Function Declarations
# Function to extract digits and return them in the form of a list.
def extract_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits

#  Function to reverse a given integer
def reverse(number):
    reverse_number = 0
    while number > 0:
        remainder = number % 10
        number //= 10
        reverse_number = reverse_number * 10 + remainder
    return reverse_number

def alternative_product(number):
    number_list = extract_digits(number)[::-1]
    odd_product = number_list[0] * number_list[2]
    even_product = number_list[1] * number_list[3]
    difference = odd_product - even_product
    return difference

# Main Program

# Taking the number as user input
print()
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
3. Difference between the product of digits at the odd position and the product of digits at the even position.
4. Exit
"""
while yes:
    print(content)
    choice = int(input("Enter your choice: "))
    print()
    print("______________________________________________________________________________________________")
    print()
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
        # Program to find the difference of products in odd and even positions of the number
        difference_of_products = alternative_product(number)
        print(f"The difference of the products of digits in odd and even places is {difference_of_products}")
    elif choice == 4:
        print("Thank you for using the program!")
        yes = False
    else:
        print("Please enter a valid choice!")
    print("______________________________________________________________________________________________")
    print()