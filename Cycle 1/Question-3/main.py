# Functions
def read_data():
    name = input("Enter the employee's name: ")
    code = input("Enter the employee's code: ")
    basic_pay = float(input("Enter the employee's basic pay: "))
    return name,code,basic_pay


def find_gross_salary(basic_pay,da,hra,ma):
    gross_salary = basic_pay + da + hra + ma
    return gross_salary

def find_deduction(pt,pf,it):
    deduction = pt + pf + it
    return deduction


def find_net_salary(gross_salary,deduction):
    net_salary = gross_salary - deduction
    return net_salary

def generate_payment_slip(name,code,basic_pay):
    if basic_pay < 10000:
        da = (5/100) * basic_pay
        hra = (2.5/100) * basic_pay
        ma = 500
        pt = 20
        pf = (8/100) * basic_pay
        it = 0.0
    elif basic_pay >= 10000 and basic_pay < 30000:
        da = (7.5/100) * basic_pay
        hra = (5/100) * basic_pay
        ma = 2500
        pt = 60
        pf = (8/100) * basic_pay
        it = 0.0
        # Complete the code here
    elif basic_pay >= 30000 and basic_pay < 50000:
        da = 0.2 * basic_pay
        hra = 0.25 * basic_pay
        ma = 0.1 * basic_pay
        pt = 0.0
        pf = 0.1 * basic_pay
        it = 0.0
    elif basic_pay >= 50000:
        da = 0.3 * basic_pay
        hra = 0.35 * basic_pay
        ma = 0.15 * basic_pay
        pt = 0.0
        pf = 0.1 * basic_pay
        it = 0.0
    # print("Name: ",name)
    # print("Code: ",code)
    # print("Basic Pay: ",basic_pay)
    # print("DA: ",da)
    # print("HRA: ",hra)
    # print("MA: ",ma)
    # print("Gross Salary: ",gross_salary)
    # print("PT: ",pt)
    # print("PF: ",pf)
    # print("IT: ",it)
    # print("Deduction: ",deduction)
    # print("Net Salary: ",net_salary)


# Gross Salary = Basic Pay + DA + HRA + MA