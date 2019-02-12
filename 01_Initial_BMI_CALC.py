"""
To calculate BMI
Extending further by using for loop
To calculate Inches feet*12+inches
To Calculate Centimeters inch*2.54
To Calculate Meters = CM/100
"""
import math
# Defiining function to calculate meters  entering feet and inches

def meters(h_ft, h_inc):
    h_inc += h_ft*12
    h_cm = round(h_inc*2.54)
    h_Met = float(round(math.sqrt(h_cm/100),1))
    print("In Meters:", h_Met)
    U_hgt = float(h_Met)
    return U_hgt

# Defining BMI Calculation
def BMI(U_wgt,U_hgt):
    BMI_CALC = (round(U_wgt/U_hgt,1))
    print("BODY MASS INDIX", BMI_CALC)
    return BMI_CALC

def BMI_Meaning(str_name,int_age):
    if BMI_CALC>=30:
        print("Obese", "Name:=", str_name, "Age:=", int_age)
    elif BMI_CALC>=29.9 and BMI_CALC<=25:
        print("Over Weight", "Name:=", str_name, "Age:=", int_age)
    elif BMI_CALC>=24.9 and BMI_CALC<=18.6:
        print("Healthy", "Name:=", str_name, "Age:=", int_age)
    else:
        print("Thin", "Name:=", str_name, "Age:=", int_age)
          
    return
# starting of the Program
names = []
Age = []
i =1
count = int(input("How Many entries:"))
while i <= count:
    str_name = str(input("Enter the Name:"))
    int_age = int(input("Enter the age:"))
#    names.append(str_name)
#    Age.append(int_age)
    h_ft = int(input("Enter Feet:"))
    h_inc = int(input("Enter Inches:"))
    U_wgt = int(input('Enter Weight:'))

    U_hgt = meters(h_ft, h_inc)
    BMI_CALC = float(BMI(U_wgt,U_hgt))
    BMI_Meaning(str_name,int_age)
    if i == count:
        break
    names.append(str_name)
    Age.append(int_age)
    i += 1
print(names)
print(Age)
