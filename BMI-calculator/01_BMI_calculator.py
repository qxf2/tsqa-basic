"""              
We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters

Exercise 1:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user 
        comes in underweight ,normal weight , overweight or obesity.
            i)Get user weight in kg 
            ii)Get user height in meter
            iii) Use this formula to calculate the bmi
                    BMI = weight_of_the_user/(height_of_the_user * height_of_the_user) 
                         
"""

print("Enter the weight of the user in Kg's")
# Get the weight of the user through keyboard
weight_of_the_user = input()

# Get the height of the user through keyboard
print("Enter the height of the user in meters")
height_of_the_user = input()

# Calculate the BMI of the user according to height and weight
bmi_of_the_user = weight_of_the_user/(height_of_the_user * height_of_the_user)

print("BMI of the user is :",bmi_of_the_user)