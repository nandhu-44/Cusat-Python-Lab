# Function Declarations

# Function to print all possible substrings
def print_all_substring(string):
    for i in range(len(string)):
        for j in range(i, len(string)):
            print(string[i:j+1])

print_all_substring("abc")