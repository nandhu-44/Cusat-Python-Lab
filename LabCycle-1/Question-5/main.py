"""
5. Develop a program to read a string and perform the following operations:
•  Print all possible substrings.
•  Print all possible substrings of length K.
•  Print all possible substrings of length K with N distinct characters.
•  Print substring(s)of length maximum length with N distinct characters.
•  Print all palindrome substrings.Define function for each of the task
"""

# Function Declarations
# Function to return all possible substrings
def all_substrings(string):
    substrings = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            substrings.add(string[i:j+1])
    return list(substrings)

# Function to return all possible substrings of length K
def substrings_of_length_k(string, k):
    if k > len(string):
        return []
    substrings = all_substrings(string)
    k_length_substrings = []
    for i in substrings:
        if len(i) == k:
            k_length_substrings.append(i)   
    return k_length_substrings

# Function to return all possible substrings of length K with N distinct characters
def substrings_of_length_k_n_distinct(string, k, n):
    if k > len(string) or n > len(string) or n > k:
        return []
    substrings = substrings_of_length_k(string, k)
    substrings_n_distinct = []
    for i in substrings:
        if len(set(i)) == n:
            substrings_n_distinct.append(i)
    return substrings_n_distinct
    
# Function to return substring(s) of length maximum length with N distinct characters
def max_substring_n_distinct(string, n):
    substrings = []
    for i in range(0,len(string)+1):
        for j in range(i+1,len(string)+1):
            s = string[i:j]
            distinct = set(s)
            if len(distinct) == n:
                substrings.append(s)
    max_len = len(max(substrings, key=len))
    return [i for i in substrings if len(i) == max_len]


# Function to return all palindrome substrings
def palindrome_substrings(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                substrings.append(string[i:j+1])
    substrings = list(set(substrings))
    return sorted(substrings)

# Function to iterate the list and return a string
def list_to_string(list):
    string = ""
    for i in list:
        string += f"{i}, "
    return string[:-2]
    
# Function to remove duplicates from a list
def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

# Main Program
# Read string from user
print()
string = input("Enter the string: ")
print()

yes = True
content = """
1. Print all possible substrings.
2. Print all possible substrings of length K.
3. Print all possible substrings of length K with N distinct characters.
4. Print substring(s)of length maximum length with N distinct characters.
5. Print all palindrome substrings.
6. Exit
"""
while yes:
    print(content)
    choice = int(input("Enter your choice: "))
    print()
    print("______________________________________________________________________________________________")
    print()
    if choice == 1:
        output = list_to_string(remove_duplicates(all_substrings(string)))
        print(f"All possible substrings are : {output}")
    elif choice == 2:
        k = int(input("Enter length of substring: "))
        output_list = substrings_of_length_k(string, k)
        if len(output_list) == 0:
            print(f"No substring of length {k} exists!")
        else:
            output = list_to_string(remove_duplicates(output_list))
            print(f"All possible substrings of length {k} are : {output}")
    elif choice == 3:
        k = int(input("Enter length of substring: "))
        n = int(input("Enter number of distinct characters: "))
        output = list_to_string(remove_duplicates(substrings_of_length_k_n_distinct(string, k, n)))
        if len(output) == 0:
            print(f"No substring of length {k} with {n} distinct characters exists!")
        else:
            print(f"All possible substrings of length {k} with {n} distinct characters are : {output}")
    elif choice == 4:
        n = int(input("Enter number of distinct characters: "))
        output = list_to_string(remove_duplicates(max_substring_n_distinct(string, n)))
        if len(output) == 0:
            print(f"No substring of length maximum length with {n} distinct characters exists!")
        else:
            print(f"Substring(s) of length maximum length with {n} distinct characters are : {output}")
    elif choice == 5:
        output = list_to_string(remove_duplicates(palindrome_substrings(string)))
        if len(output) == 0:
            print("No palindrome substring exists!")
        else:
            print(f"All palindrome substrings are : {output}")
    elif choice == 6:
        print("Thank you for using the program!")
        yes = False
    else:
        print("Please enter a valid choice!")
    print("______________________________________________________________________________________________")
    print()