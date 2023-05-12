"""
1. Suppose a newly born pair of rabbits, one male and one female, are
put in a field. Rabbits can mate at the age of one month so that at the
end of its second month, a female has produced another pair of
rabbits. Suppose that our rabbits never die and that the female always
produces one new pair every month from the second month.
Develop a program to show a table containing the number of pairs of
rabbits in the first N months.
"""
# Importing tabulate module to print the table
from tabulate import tabulate

#  Function to calculate the number of pairs of rabbits in the first N months
def calculate_rabbits(months):
    if months == 1 or months == 2:
        return 1
    else:
        return calculate_rabbits(months - 1) + calculate_rabbits(months - 2)


# Main program
months = int(input("Enter the number of months: "))

# Printing the table
rabbit_table = [[i, calculate_rabbits(i)] for i in range(1, months + 1)]
print(tabulate(rabbit_table, headers=[
      "Month", "Number of pairs of rabbits"], tablefmt="fancy_grid"))