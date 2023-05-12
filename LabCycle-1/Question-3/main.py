"""
3. Develop a program to read the employee's name, code, and basic pay
and calculate the gross salary, deduction, and net salary according to
the following conditions. Define a function to find each of the
components. Finally, generate a payslip.
"""

# Function Declarations
# Function to read the name code and basic pay of employee
def read_data():
    name = input("Enter the employee's name: ")
    code = input("Enter the employee's code: ")
    basic_pay = float(input("Enter the employee's basic pay: "))
    return name,code,basic_pay

# Function to calculate gross salary
def find_gross_salary(basic_pay,da,hra,ma):
    # Gross Salary = Basic Pay + DA + HRA + MA
    gross_salary = round(basic_pay,2) + round(da,2) + round(hra,2) + round(ma,2)
    return gross_salary
# Function to calculate deduction
def find_deduction(pt,pf,it):
    # Deduction = PT+ PF + IT
    deduction = round(pt,2) + round(pf,2) + round(it,2)
    return deduction

# Function to calculate net salary
def find_net_salary(gross_salary,deduction):
    # Net Salary = Gross Salary - Deduction
    net_salary = gross_salary - deduction
    return net_salary
# Function to generate payment slip
def generate_payment_slip(name,code,basic_pay):
    # Calculate DA, HRA, MA, PT, PF, IT based on basic pay
    if basic_pay < 10000:
        da = (5/100) * basic_pay
        hra = (2.5/100) * basic_pay
        ma = 500
        pt = 20
        pf = (8/100) * basic_pay
        it = 0
    elif basic_pay >= 10000 and basic_pay < 30000:
        da = (7.5/100) * basic_pay
        hra = (5/100) * basic_pay
        ma = 2500
        pt = 60
        pf = (8/100) * basic_pay
        it = 0
    elif basic_pay >= 30000 and basic_pay < 50000:
        da = (11/100) * basic_pay
        hra = (7.5/100) * basic_pay
        ma = 5000
        pt = 60
        pf = (11/100) * basic_pay
        it = (11/100) * basic_pay
    elif basic_pay >= 50000:
        da = (25/100) * basic_pay
        hra = (11/100) * basic_pay
        ma = 7000
        pt = 80
        pf = (12/100) * basic_pay
        it = (20/100) * basic_pay
    gross_salary = find_gross_salary(basic_pay,da,hra,ma)
    deduction = find_deduction(pt,pf,it)
    net_salary = find_net_salary(gross_salary,deduction)
    print()
    print("__PAYMENT SLIP__")
    # Replace shortforms with full forms
    content = f"""
Employee Name               :    {name}
Employee Code               :    {code}
Basic Pay                   :   ₹{round(basic_pay, 2)}
Dearness Allowance (DA)     :   ₹{round(da, 2)}
House Rent Allowance (HRA)  :   ₹{round(hra, 2)}
Medical Allowance (MA)      :   ₹{round(ma, 2)}
Professional Tax (PT)       :   ₹{round(pt, 2)}
Provident Fund (PF)         :   ₹{round(pf, 2)}
Income Tax (IT)             :   ₹{round(it, 2)}
Gross Salary                :   ₹{gross_salary}
Deduction                   :   ₹{deduction}
Net Salary                  :   ₹{net_salary}
"""
    print(content)

# Main Program

yes = True
content = """
______ Main Menu ______
1. Generate Payment Slip
2. Exit
"""
while yes:
    print(content)
    choice = int(input("Enter your choice: "))
    print()
    print("______________________________________________________________________________________________")
    print()
    if choice == 1:
        # Take input from user and generate payment slip
        name,code,basic_pay = read_data()
        generate_payment_slip(name,code,basic_pay)
    elif choice == 2:
        print("Thank you for using the program! ")
        yes = False
    else:
        print("Please enter a valid choice!")
    print("______________________________________________________________________________________________")
    print()