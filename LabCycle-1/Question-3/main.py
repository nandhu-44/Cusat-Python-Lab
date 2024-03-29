"""
3. Develop a program to read the employee's name, code, and basic pay
and calculate the gross salary, deduction, and net salary according to
the following conditions. Define a function to find each of the
components. Finally, generate a payslip.
"""

# Function to read the name code and basic pay of employee
def read_data():
    name = input("Enter the employee's name: ")
    code = input("Enter the employee's code: ")
    basic_pay = float(input("Enter the employee's basic pay: "))
    return name,code,basic_pay

# Function to calculate gross salary
def find_gross_salary(basic_pay,da,hra,ma):
    return round(basic_pay,2) + round(da,2) + round(hra,2) 
    + round(ma,2)

# Function to calculate deduction
def find_deduction(pt,pf,it):
    deduction = round(pt,2) + round(pf,2) + round(it,2)
    return deduction

# Function to calculate net salary
def find_net_salary(gross_salary,deduction):
    net_salary = gross_salary - deduction
    return net_salary
# Function to generate payment slip
def generate_payment_slip(name,code,basic_pay):
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
    print("\n-----PAYMENT SLIP-----")
    print(f"""
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
""")

# Main program
name,code,basic_pay = read_data()
generate_payment_slip(name,code,basic_pay)