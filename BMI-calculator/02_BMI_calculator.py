"""
Exercise 2:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user 
        comes in underweight ,normal weight or obesity.
            i)Get user weight in kg 
            ii)Get user height in meter
            iii) Use this formula to calculate the bmi
                    BMI = weight_of_the_user/(height_of_the_user * height_of_the_user)
            iv)Use this level to check user category
                #)Less than or equal to 18.5 is represents underweight
                #)Between 18.5 -24.9 indicate normal weight
                #)Between 25 -29.9 denotes over weight
                #)Greater than 30 denotes obese

We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters
"""

print "Enter the weight of the user in Kg's"
# Get the weight of the user through keyboard
weight_of_the_user = input()

# Get the height of the user through keyboard
print "Enter the height of the user in meters"
height_of_the_user = input()

# Calculate the bmi of the user according to height and weight
bmi = weight_of_the_user/(height_of_the_user * height_of_the_user)

print 'bmi of the user is : ' , bmi

# Check the user comes under under weight, normal or obesity
if bmi <= 18.5:
    print 'The user is considered as underweight'
elif bmi > 18.5 and bmi < 24.9:
    print 'The user is considered as normal weight'
elif bmi > 25 and bmi <= 29.9:
    print 'The user is considered as overweight'
elif bmi >=30:
    print 'The user is considered as obese'


