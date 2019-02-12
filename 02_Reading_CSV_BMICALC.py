"""
To calculate BMI
Extending further by reading the CSV file
To calculate Inches feet*12+inches
To Calculate Centimeters inch*2.54
To Calculate Meters = CM/100
Compare the BMI of the user which you have calculated and the player’s BMI which are stored in the CSV file
"""
import math,os
# Defiining function to calculate meters  entering feet and inches
def meters(h_ft, h_inc):
    h_inc += h_ft*12
    h_cm = round(h_inc*2.54)
    h_Met = float((h_cm/100))
    print("In Meters:", h_Met)
    U_hgt = round(math.pow(h_Met,2))
    return U_hgt
# Defining BMI Calculation
def BMI(U_wgt,U_hgt):
    BMI_CALC = (round(U_wgt/U_hgt,1))
    print("BODY MASS INDEX", BMI_CALC)
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
#Comparing the calculated value with csv and displaying the name.

def compare_userBMI_from_csv(all_lines):
    global BMI_CALC
   
    # Calls the all players data fetch BMI value
    for each_line in all_lines:
        if BMI_CALC == float(each_line.split(',')[3]):
            csvusr_name = each_line.split(',')[0]
            print(csvusr_name)
        else:
                print("No Matching found")
                break
        
# Opening/Reading CSV file
def readall_players_data_csv_file():
    "This functions reads the players CSV file"
    # To read the CSV file we have to join the path where it's located       
    filename = os.path.abspath(os.path.join('..','/Raghava/tsqa-basic/data',"all_players_data.csv"))
    # To open the text file and assign to object fp
    with open(filename,"r") as fp:
        all_lines = fp.readlines()
        compare_userBMI_from_csv(all_lines)
# starting of the Program
def entry_pointfor_BMI():
    global BMI_CALC
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
        readall_players_data_csv_file()
        BMI_Meaning(str_name,int_age)
        if i == count:
            break
        i += 1
# Program starts here
if __name__ == "__main__":
    # This is the calling function to read the CSV file 
    entry_pointfor_BMI()
