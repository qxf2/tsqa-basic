"""
We will use this script to teach Python to absolute beginners
The script is an example of salary  calculation implemented in Python
We read the CSV files and calcuate the take home salary of each employee
The salary calculator: 
    Net_Income = Gross_Income - Taxable_Due
    Taxable_Due = taxable_income + Social_security + Medicare_tax
    Taxable_Income = Gross_Income -120,00
    Social_security = 6.2% of Gross_Income
    Medicare_Tax = 1.45 % of Gross_Income
Federal tax brackets
10%	$0 to $9,525	
12%	$9,526 to $38,700	
22%	$38,701 to $82,500	
24%	$82,501 to $157,500	
32%	$157,501 to $200,000	
35%	$200,001 to $500,000	
37%	$500,001 or more
"""

# Importing the OS module to make use in this program.
import os

def employee_federal_tax(employee_name,taxable_income):
    "This method calculates the employee federal tax brackets"    
    tax_bracket = [9525,29175,43799,74999,42499,299999,500000]
    tax_rate = [10,12,22,24,32,35,37]
    sigma_of_federal_tax = 0
    if taxable_income >= 500001:
        for i in range(6):
            federal_tax_bracket = ((tax_rate[i]*tax_bracket[i])/100)        
            sigma_of_federal_tax = federal_tax_bracket + sigma_of_federal_tax        
        federal_tax = sigma_of_federal_tax + (((taxable_income-500001)*37)/100)        

    elif taxable_income > 200001 and taxable_income <= 500000:
        for i in range(5):
            federal_tax_bracket = ((tax_rate[i]*tax_bracket[i])/100)        
            sigma_of_federal_tax = federal_tax_bracket + sigma_of_federal_tax        
        federal_tax = sigma_of_federal_tax +  (((taxable_income-200001)*35)/100)            

    elif taxable_income > 157501 and taxable_income <= 200000:
        for i in range(4):
            federal_tax_bracket = ((tax_rate[i]*tax_bracket[i])/100)        
            sigma_of_federal_tax = federal_tax_bracket + sigma_of_federal_tax        
        federal_tax = sigma_of_federal_tax +  (((taxable_income-157501)*32)/100)          
            
    elif taxable_income > 82501 and taxable_income <= 157500:
        for i in range(3):
            federal_tax_bracket = ((tax_rate[i]*tax_bracket[i])/100)        
            sigma_of_federal_tax = federal_tax_bracket + sigma_of_federal_tax        
        federal_tax = sigma_of_federal_tax +  (((taxable_income-82501)*24)/100)             

    elif taxable_income > 38701 and taxable_income <= 82500:
        for i in range(2):
            federal_tax_bracket = ((tax_rate[i]*tax_bracket[i])/100)        
            sigma_of_federal_tax = federal_tax_bracket + sigma_of_federal_tax        
        federal_tax = sigma_of_federal_tax +  (((taxable_income-38701)*22)/100)              

    elif taxable_income >= 9525 and taxable_income <= 38700:
        for i in range(1):
            federal_tax_bracket = ((tax_rate[i]*tax_bracket[i])/100)        
            sigma_of_federal_tax = federal_tax_bracket + sigma_of_federal_tax        
        federal_tax = sigma_of_federal_tax +  (((taxable_income-9526)*12)/100)         

    elif taxable_income >0 and taxable_income < 9525:
        federal_tax = ((taxable_income *10)/100)

    else:
        federal_tax =0
        print("The employee no need to pay the federal tax")

    # print("federal tax is %s") %employee_name,federal_tax
    print("The federal tax for %s is %s"% (employee_name,federal_tax))
    return federal_tax

def employee_take_homes_salary(employee_name,employee_gross_income,federal_tax):
    "This function calculates the employee take home salary"
    # 6.2% of gross income is social security
    social_security = ((float(employee_gross_income) *6.2)/100)
    if social_security >= 7960.80:
        social_security = 7960
    print("The social security for %s is %s"%(employee_name,social_security))

    # 1.45% of gross income is medicare tax
    medicare_tax = float(employee_gross_income) *(1.45/100)
    print("The medicare tax for %s is %s"%(employee_name,medicare_tax))

    # Taxable due
    taxable_due = federal_tax + social_security + medicare_tax

    # Net income(Take home salary)
    net_income = round(float(employee_gross_income) - taxable_due,2)    

    return net_income

def calculate_take_home_salary(all_lines):
    "Calls the federal tax,employee take home salary function"
    taxable_deduction = 12000              
    for each_line in all_lines:            
        # Fetch the employee name from the file           
        employee_name = each_line.split(',')[0]
                                
        # Fetch the employee gross income from the file          
        employee_gross_income = each_line.split(',')[6]

        # Taxable income
        taxable_income = (float(employee_gross_income)) - taxable_deduction

        # This is the calling function to calculate the federal tax
        federal_tax = employee_federal_tax(employee_name,taxable_income)

        # This is the calling function to calculate the employee take home salary
        net_income = employee_take_homes_salary(employee_name,employee_gross_income,federal_tax)
        print("The %s take home salary is %s"%(employee_name,net_income))
        print("------------------------------------------------------------------")           
       
def read_employee_salary_csv_file():
    "This functions reads the CSV file"
    # To read the CSV file we have to join the path where it's located 
    path = "C:\\Users\\Rahul Bhave Qxf2\\code\\rahul-qxf2"      
    filename = os.path.abspath(os.path.join(path,"tsqa-basic\\data","employee_payroll.csv"))

    # To open the text file and assign to object fp
    with open(filename,"r") as fp:
        all_lines = fp.readlines()
    # Calling the function to calculate the salray    
    calculate_take_home_salary(all_lines)
    
# Program starts here
if __name__ == "__main__":
    # This is the calling function to read the CSV file 
    read_employee_salary_csv_file()    