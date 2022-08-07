""" We will use Python scripts for absolute beginners
 This script shows the use of BMR Calculator = Basal Metabolic Rate Calculator.
 BMR gives the value of the calories which the body intakes during weight gain or weight loss.
 The BMR Calculator:
    # Get the Age of the user
    # Get the Gender of the user
    # Get the weight(Kg/lb) of the user
    # Get the height(m/in") of the user
    # Calculate the BMI using the formula on the basis of gender, age, height and weight
       For Male: BMR= 88.362+(13.397*weight in kg/lb)+(4.799*height in cm/in")- (5.677*age in years)
       For Female: BMR = 447.593+(9.247*weight in kg/ib)+(3.098*height in cm/in")- (4.330*age in years)
       Also, this BMR calculator include features in Metric Units (kg,metre) & American Units (pound, inch)

Exercise 1: Calculate the BMR (in calorie)
Exercise 2: Check if the no. of days workout the user does:
            No. of Days       BMR *Value      Level of Intensity
                0-1             BMR*1.2         NO Exercise
                1-3            BMR*1.375       Light Exercise
                3-5            BMR*1.55       Moderate Exercise
              All Day          BMR*1.725       Heavy Exercise
Here there will be an implication of User-defined functions and Calling function along with if else statement.
"""
import os
import configparser
import helper
subject_file = configparser.ConfigParser()


print("*****Welcome To The BMR Calculator*****")
def __getinput_to_calculate_bmr():
    "This function gets the input from the user "
    Units_of_the_user = input("Metric or American:")
    if Units_of_the_user == 'Metric':
        print("Enter Weight in kg and Height in meters")
    elif Units_of_the_user == 'American':
        print("Enter Weight in pound and Height in inches")
    Weight_of_the_user = float(input("Enter the weight of the user:"))
    Height_of_the_user = float(input("Enter the height of the user:"))
    Gender_of_the_user = (input("Enter the gender of the user M/m or F/f:")).lower()
    Age_of_the_user = int(input("Enter the age of the user:"))



    return Weight_of_the_user, Height_of_the_user, Age_of_the_user,Units_of_the_user, Gender_of_the_user

def calculate_bmr (Weight_of_the_user, Height_of_the_user, Age_of_the_user,Units_of_the_user, Gender_of_the_user):
    " This function calculates the BMR in metric OR american units on the basis of gender and age "

     # Here if the Gender_of_the_user is 'M' i.e Male, then formula will be:
    if Gender_of_the_user ==  Units_of_the_user:
        BMR = round(Metric + (Weight * Weight_of_the_user) + (Height * Height_of_the_user)- (Age*Age_of_the_user))
        return BMR

    # Here if the Gender_of_the_user is 'F' i.e Female, then formula will be:
    elif Gender_of_the_user == Units_of_the_user:
        BMR = round(Metric + (Weight1 * weight_of_the_user) + (Height1 * height_of_the_user)- (Age1*Age_of_the_user))
        return BMR

    # Here if the Gender_of_the_user is 'M' i.e Male, and taken in American Units (Weights and Heights of the user is pound and inch respectively
    # then formula will be:
    elif Gender_of_the_user == Units_of_the_user:
        BMR = round(American + (Weight * weight_of_the_user*pound) + (Height * height_of_the_user*inch) - (Age * Age_of_the_user))
        return BMR

    # Here if the Gender_of_the_user is 'F' i.e Female, and taken in American Units (Weights and Heights of the user is taken into pound and inch respectively
    # then formula will be:
    elif Gender_of_the_user == Units_of_the_user:
        BMR = round(American + (Weight1 * weight_of_the_user*pound) + (Height1 * height_of_the_user*inch) - (Age1 * Age_of_the_user))
        return BMR



def check_user_BMR_category(BMR):
    "This function checks if the user's Level of Intesity is No Exercise, Light Exercise, Moderate Exercise, Heavy Weight Exercise, Severy Heavy Weight Exercise"

    "The BMR values will be calculated. Then it will be multiplied with standard numbers will categorized the level of intensity/activeness the user's lifestyle "

    "If User's BMR is: Calorific Value= BMR*Standard Numbers which will denote the intensity of the user. "
    Calorific_Value = BMR*1.2
    Calorific_Value1 =BMR*1.375
    Calorific_Value2 = BMR*1.55
    Calorific_Value3 = BMR*1.725

    if  BMR>800 and BMR<=1100:
        print("The Value of the calorie intake is:", Calorific_Value, "which means : Minimal Exercise (1 Day)!!")
    elif BMR >=1200 and BMR <=1400:
        print("The Value of the calorie intake is:", Calorific_Value1, "which means : Light Exercise (1-3 Days)!!")
    elif BMR >=1450 and BMR <=1700:
        print("The Value of the calorie intake is:", Calorific_Value2, "which means :Moderate Exercise (3-5 Days)!!")
    elif BMR>2000:
        print("The Value of the calorie intake is:", Calorific_Value3, "which means :Heavy Weight Exercise (7 days)")



if __name__ == "__main__":

    #subject_file.read()
    with open("Config.ini") as subjectfileObj:
        subject_file.write(subjectfileObj)
        subjectfileObj.flush()
        subjectfileObj.close()
        print("subject file 'Config.ini' is created")
        #print(d2.keys())

    # This calling function gets the input from the user
    weight_of_the_user, height_of_the_user, Units_of_the_user, Gender_of_the_user, age_of_the_user = __getinput_to_calculate_bmr()

    # This calling function stores the BMI of the user
    BMR_value = calculate_bmr(weight_of_the_user, height_of_the_user, Units_of_the_user, Gender_of_the_user,age_of_the_user)

    print("BMR of the user is :", BMR_value )

    # This function is used to calculate the user's criteria
    check_user_BMR_category(BMR_value)



