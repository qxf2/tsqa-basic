"""
We will use this script to teach Python to absolute beginners
The script is an example of salary  calculation implemented in Python
The salary calculator: 
    Net_Income = Gross_Income - Taxable_Due
    Taxable_Due = Federal_tax + Social_security + Medicare_tax
    Taxable_Income = Gross_Income -120,00
    Social_security = 6.2% of Gross_Income
    Medicare_Tax = 1.45 % of Gross_Income
"""

# Enter the gross income
print("Enter the gross income")

# raw_input gets the input from the keyboard through user
gross_income = float(input())

# Enter the federal tax
print("Enter the federal_tax")

# Getting the federal tax from the user
fedral_tax = float(input())

# Taxable income will be reduced from gross income.This is the fixed dedutable income
taxable_deduction = 12000

# 6.2% of gross income is social security
social_security = gross_income *(6.2/100)
print("The employee social_security is",social_security)

# 1.45% of gross income is medicare tax
medicare_tax = gross_income *(1.45/100)
print("The employee medicare tax is",medicare_tax)

# Taxable due
taxable_due = fedral_tax + social_security + medicare_tax

# Net income
net_income = gross_income - taxable_due

print("The employee take home salary is",net_income)