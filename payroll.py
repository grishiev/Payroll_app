# Imports


# Globals

weeks_annually = 52
    # PAYE:
        # Tax credits
tax_credit_single = 1775
tax_credit_employee = 1775

        # Tax rate cut off
tax_rate_cutoff_low = 40000
        
        # Low rate
tax_rate_low = 0.2

        # High rate
tax_rate_high = 0.4
        
    # USC

    # PRSI
    # Max PRSI credit
prsi_credit = 12

    # List of employees
        # First name
        # Last name
        # PPSN
        # Personal tax credit
        # PRSI class
        # Annual salary amount

employee1 = {"First name": "John", "Last name": "Appleseed", "PPSN": "1234567AB",
            "Personal tax credit": tax_credit_single, "PRSI class": "A",
            "Annual salary amount": 40000}

employee2 = {"First name": "Joe", "Last name": "Dow", "PPSN": "1267673AZ",
            "Personal tax credit": tax_credit_single, "PRSI class": "A",
            "Annual salary amount": 65000}

employee3 = {"First name": "Eve", "Last name": "Adamson", "PPSN": "1290273KZ",
            "Personal tax credit": tax_credit_single, "PRSI class": "A",
            "Annual salary amount": 78000}

employees = []
employees.append(employee1)
employees.append(employee2)
employees.append(employee3)


# Functions

def start_menu():
    print("\n   Welcome to the Payroll!!!\n---------------------------------\n")
    print("Type -1- to View the list of employees")
    print("Type -2- to Add an employee")
    print("Type -3- to Print a payslip")
    print("Type -4- to Print all payslips")
    print("Type -5- to Show annual payroll total")
    print("Type -6- to Show monthly payroll total")
    print("Type -7- to Show weekly payroll total")
    print("Type -h- for Help")
    print("Type -0- to Exit")

def view_employees():
    num = 1
    for e in employees:
        print(f'Employee {num} - Name: {e["First name"]} {e["Last name"]} PPSN: {e["PPSN"]} Salary: ${e["Annual salary amount"]}') 
        num += 1

def add_employee(details):

    f_name, l_name, pps, credit_t, prsi, sal = details

    print(f"{f_name} {l_name} {pps} {credit_t} {prsi} {sal}")

    new_employee = {"First name": f_name, "Last name": l_name, "PPSN": pps,
            "Personal tax credit": credit_t, "PRSI class": prsi,
            "Annual salary amount": sal}
    employees.append(new_employee) 
    view_employees()
    # new_employee = dict()
    # new_employee["First name"] = input("Add first name: ").strip().capitalize()
    # new_employee["Last name"] = input("Add last name: ").strip().capitalize()
    # new_employee["PPSN"] = input("Add PPSN: ")
    # new_employee["Personal taxt credit"] = tax_credit_single
    # new_employee["PRSI class"] = input("Add the PRSI class: ")
    # new_employee["Annual salary amount"] = int(input("Add employee salary: "))
    
    # employee_details()
    # employees.append(new_employee)

def employee_details():
    first_name = ""
    last_name = ""
    ppsn = ""
    tax_credit = 0
    prsi_class = ""
    salary = 0


    # First name (the variable must be in the loop for it to work)
    
    while True:
        first_name = input("Add employee first name: ").strip().capitalize()
        if len(first_name) >= 2:
            print(first_name)
            break
        else:
            print("Please, enter a valid first name: ")
    
    # Last name (if the variable outside the loop, the else should assign a value to the variable)
    last_name = input("Add employee last name: ").strip().capitalize()
    while True:
        if len(last_name) >= 2:
            print(last_name)
            break
        else:
            last_name = input("Please, enter a valid last name: ")

# PPSN - 8 or 9 characters long and first 7 are numbers

    while True:
        ppsn = input("Add employee PPSN: ").strip()
        if len(ppsn) == 8 and ppsn[:7].isdigit() and ppsn[-1].isalpha():
            print(ppsn)
            break
        elif len(ppsn) == 9 and ppsn[:7].isdigit() and ppsn[-2:].isalpha():
            print(ppsn)
            break
        else:
            ppsn = input("Invalid entry. PPSN should be 8 or 9 characters long. Please, try again ")

# Tax credit
    while True:
        tax_credit_string = input("Add employee tax credit: ").strip()
        
        arr = tax_credit_string.split(".")
        arr_count = len(arr)
        
        if arr_count < 3:
            if "." in tax_credit_string and len(tax_credit_string) > 1:
                tax_credit = float(tax_credit_string)
                print(tax_credit)
                break
            elif tax_credit_string.isnumeric():
                tax_credit = int(tax_credit_string)
                print(tax_credit)
                break
            else:
                print("Invalid entry. Tax credit must be a number: ")
        else:
            print("Invalid entry. Tax credit must contain no more than 1 decimal point")

    # Tax credit class
    while True:
        prsi_class = input("Add employee PRSI class: ")
        if len(prsi_class) == 2 and prsi_class[:1].upper() == "A":
            print(prsi_class)
            break
        else:
            print("Invalid entry. PRSI class must begin with 'A' and be 2 characters in length")

# Salary

    while True:
        salary_string = input("Add employee salary: ").strip()
        
        arr = salary_string.split(".")
        arr_count = len(arr)
        
        if arr_count < 3:
            if "." in salary_string and len(salary_string) > 1:
                salary = float(salary_string)
                print(salary)
                break
            elif salary_string.isnumeric():
                salary = int(salary_string)
                print(salary)
                break
            else:
                print("Invalid entry. Salary must be a number: ")
        else:
            print("Invalid entry. Salary must contain no more than 1 decimal point")

    print(f'{first_name} {last_name} {ppsn} {tax_credit} {prsi_class} {salary}')
    return first_name, last_name, ppsn, tax_credit, prsi_class, salary



def get_annual_paye(employee):
    annual_salary = employee["Annual salary amount"]
    high_rate_amount = 0.00
    low_rate_amount = 0.00
    tax_liability = 0.00
    tax_credit = employee["Personal tax credit"] + tax_credit_employee
    
# if annual salary > 40.000, anything above that figure is calculated at 40%
# Anything aup to this sum is calculated at 20%. Minus tax credits
# (20%+40%) - credit = payee liability

    if annual_salary > tax_rate_cutoff_low:
        #calculate 40% amount
        high_rate_amount = (annual_salary - tax_rate_cutoff_low)*tax_rate_high
    else:
        low_rate_amount = annual_salary*tax_rate_low

    tax_liability = (high_rate_amount + low_rate_amount) - tax_credit
    return tax_liability

def weekly_prsi_employee(employee):
    prsi = 0.00
    prsi_credit = 0.0
    weekly_gross = employee["Annual salary amount"]/weeks_annually

    # if the employee is PRSI class A and earns less than $352.01, the pay $0
    # If they earn between $352.01 and $441 they pay 4% minus their PRSI credit

    # The credit does not apply to anything over $424.01

    if weekly_gross < 352.01:
        prsi = 0.00
    elif weekly_gross > 352 and weekly_gross < 424.01:
        prsi_credit_personal = prsi_credit - ((weekly_gross - 352.01)/6)
        prsi = (weekly_gross*0.04)-prsi_credit_personal
    else:
        prsi = (weekly_gross*0.04)
    
    return prsi

def weekly_prsi_employer(employee):
    prsi = 0.00
    prsi_credit = 0.0
    weekly_gross = employee["Annual salary amount"]/weeks_annually

    # if the employee is PRSI class A and earns less than $352.01, the pay $0
    # If they earn between $352.01 and $441 they pay 4% minus their PRSI credit

    # The credit does not apply to anything over $424.01

    if weekly_gross <= 441:
        prsi = weekly_gross*0.088
    else:
        prsi = (weekly_gross*0.1105)
    
    return prsi

def usc_annual(employee):
    usc = 0.00
    annual_salary = employee["Annual salary amount"]
    # Exempt if you earn < $13000
    # Otherwise:
    #
    #
    if annual_salary < 13000:
        usc = 0.00
    else:
        usc = 12012*0.005
        annual_salary = annual_salary-12012
        if annual_salary >= 10908:
            usc += 10908*0.02
            annual_salary = annual_salary-10908
        else:
            usc += annual_salary*0.02
        
        if annual_salary >= 47124:
            usc += 47124*0.045
            annual_salary = annual_salary-47124
        else:
            usc += annual_salary*0.045

        if annual_salary > 0:
            usc += annual_salary*0.08
    
    return usc


# Print a payslip for a particular employee

def print_payslip(employee):

    name = f"{employee['First name']} {employee['Last name']}"
    ppsn = employee['PPSN']
    tax_credit = (employee["Personal tax credit"] + tax_credit_employee)/weeks_annually
    prsi_class = employee["PRSI class"]
    salary = employee["Annual salary amount"]
    gross_pay = salary/weeks_annually
    annual_paye = get_annual_paye(employee)
    weekly_paye = annual_paye/weeks_annually
    employee_weekly_prsi = weekly_prsi_employee(employee)
    employer_weekly_prsi = weekly_prsi_employer(employee)
    usc_per_year = usc_annual(employee)
    if usc_per_year > 0:
        weekly_usc = usc_per_year/weeks_annually
    net_pay = ((gross_pay - weekly_paye)-employee_weekly_prsi)-weekly_usc
    
    print("\n--------------------------------------")
    print("Eir Telecom Inc.")
    print(f"Employee PPS no.: {ppsn}")
    print(f"Employee name: {name}")
    print(f"PRSI class: {prsi_class}")
    print("\n--------------------------------------")
    print(f"Gross pay: {salary/weeks_annually}")
    print(f"PAYE: {weekly_paye}")
    print(f"PRSI (employee): {employee_weekly_prsi}")
    print(f"PRSI (employer): {employer_weekly_prsi}")
    print(f"USC: {weekly_usc}")
    print("\n              -----------")
    print(f"Net pay: {net_pay}")
    print("\n--------------------------------------")
    #print(f"Employee: {name}\t PPSN: {ppsn}\t ")

def payroll_gross():
    payroll_gross = 0
    payroll_each = 0
    for e in employees:
        payroll_each = e["Annual salary amount"]
        #print(payroll_each)
        payroll_gross += payroll_each
    return payroll_gross

def help():
    print("The menue has seven option for you:\n\
if you press '1' you are be presented with the list of all employees in the company;\n\
    ------------\n\
if you press '2' you can add a new employee into the system. Keep all the data at hand,\n\
i.e. first and last name, PPSN, personal tax credit, PRSI class, and the annual salary;\n\
    ------------\n\
if you press '3' you can print a payslip for an employee you may select from the list;\n\
    ------------\n\
if you press '4' you will print the payslips for all the employees at once;\n\
    ------------\n\
if you press '5' you will be presented with the gross annual payroll expenditure;\n\
    ------------\n\
if you press '6' you will be presented with the gross monthly payroll;\n\
    ------------\n\
if you press '7' you will be presented with the gross weekly payroll;\n\
    ------------\n\
to exit the menue, press '0'.\n")

def question():
    q = input("Would you like to continue? Print 'y' for yes or 'n' for no: ")
    if q == "n":
        print("Have a nice rest of the day!")
        exit()

# Main function
def main():
    cont = True
    while cont:
        start_menu()
        option = input()
        # start_menu()
        # option = input()
        if(option == "1"):
            view_employees()
            question()

        elif(option == "2"):
            add_employee(employee_details())
            question()
        elif(option == "3"):
            view_employees()
            # A loop to check the validity of the input of the employee number
            valid = True
            while valid:
                employee_num = int(input("Please, provide the employee number: "))
                if employee_num > len(employees):
                    print("Please, enter a valid number")
                    
                else:
                    print_payslip(employees[employee_num - 1])
                    valid = False
            question()

        elif(option == "4"):
            for e in employees:
                print_payslip(e)
            question()
    # payroll annual
        elif(option == "5"):
    
        #print("The annual payroll is:", payroll_gross())
            print(f"The annual payroll is: {payroll_gross()}")
            question()
    # monthly
        elif(option == "6"):
            print(f"The monthly payroll is: {payroll_gross()/12}")
            question()
    # weekly
        elif(option == "7"):
            print(f"The weekly payroll is: {payroll_gross()/52}")
            question()
    
        elif(option == "h" or option == "H"):
            help()
            question()

        elif(option == "0"):
            print("Have a nice rest of the day!")
            cont=False
            #exit()
        else:
            print("****Error****\nPlease, provide correct input!")
# Call Main here
main()