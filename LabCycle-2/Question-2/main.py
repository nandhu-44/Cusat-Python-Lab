"""
2. Write a program to read a string containing numbers separated by a
space and convert it as a list of integers. Perform the following
operations on it.
 ● Rotate elements in a list by 'k' position to the right
 ● Convert the list into a tuple using list comprehension
 ● Remove all duplicates from the tuple and convert them
into a list again.
 ● Create another list by putting the results of the evaluation
of the function f(x) = x^2 - x with each element in the
final list
 ● After sorting them individually, merge the two lists to
create a single sorted list.
"""
# Function to convert the string to list of integers
def convert_to_list(string_numbers):
    list_of_strings = string_numbers.split(" ")
    list_of_strings = [x for x in list_of_strings if x != '']
    for i in range(len(list_of_strings)):
        list_of_strings[i] = int(list_of_strings[i])
    return list_of_strings

# Function to rotate elements in a list by 'k' position to the right
def switch_to_right(my_list,k):
    for i in range(k):
        element = my_list.pop()
        my_list.insert(0, element)
    return my_list

# Function to convert the list into a tuple using list comprehension
def generate_tuple(my_list):
    return tuple(x for x in my_list)

# Function to remove all duplicates from the tuple and convert them into a list again
def remove_duplicates(my_tuple):
    return list(set(my_tuple))

# Function to create list of f(x) = x^2 - x with each element in the final list
def evaluate_function(my_list):
    return [x**2 - x for x in my_list]

# Function to merge both the lists and sort them
def merge_and_sort(my_list1, my_list2):
    my_list1.extend(my_list2)
    my_list1.sort()
    return my_list1

# Main program
print()
# Taking input from the user and converting it to a list of integers
string_numbers = input("Enter the numbers separated by spaces: ")
list_of_strings = convert_to_list(string_numbers)

contents = """
----------------------------------------------------------------------------------------------------
-----Main Menu-----
1. Rotate elements in a list by 'k' position to the right
2. Convert the list into a tuple using list comprehension
3. Remove all duplicates from the tuple and convert them into a list again.
4. Create list of f(x) = x^2 - x with each element in the final list
5. Merge both the lists and sort them
6. Exit
"""
while True:
    print(contents)
    choice = int(input("Enter your choice: "))
    print()
    print("----------------------------------------------------------------------------------------------------")
    print()
    if choice == 1:
        k = int(input("Enter the value of k: "))
        print(f"The list after rotating by {k} position to the right is : {switch_to_right(list_of_strings.copy(), k)}")
    elif choice == 2:
        print(f"The list converted to tuple is : {generate_tuple(list_of_strings.copy())}")
    elif choice == 3:
        print(f"The list after removing duplicates is : {remove_duplicates(generate_tuple(list_of_strings.copy()))}")
    elif choice == 4:
        print(f"The list of f(x) = x^2 - x is : {evaluate_function(remove_duplicates(list_of_strings.copy()))}")
    elif choice == 5:
        print(f"The merged and sorted list is : {merge_and_sort(remove_duplicates(list_of_strings.copy()), evaluate_function(remove_duplicates(list_of_strings.copy())))}")
    elif choice == 6:
        print("Thank you for using the program.")
        break
    else:
        print("Please provide a valid choice!")
print()
