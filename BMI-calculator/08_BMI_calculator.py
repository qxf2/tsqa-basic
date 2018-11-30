"""
Exercise 3:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user comes
        in underweight ,normal weight or obesity by creating a class. Read the CSV files which contains player data and compare your BMI 
        with a player.Create functions for calculating BMI and check the user category.The class should be imported from 
        another file
       
            i)Get user weight in kg 
            ii)Get user height in meter
            iii) Use this formula to calculate the BMI
                    BMI = weight_of_the_user/(height_of_the_user * height_of_the_user)
            iv)Use this level to check user category
                #)Less than or equal to 18.5 is represents underweight
                #)Between 18.5 -24.9 indicate normal weight
                #)Between 25 -29.9 denotes over weight
                #)Greater than 30 denotes obese
        # Hint
            i)Create a class 
            iiCreate one method to calculate BMi
            iii)Create one more method for checking user category
            iv)Create one method to read the text file and compare the user BMI with players BMI

We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters
"""
# Importing the class from another file
from BMI_calculation_class import bmiCalculator

def get_input_to_calcluate_bmi():
    "This function gets the input from the user"    
    #Getting input will be repeated until the user enters the proper input
    while True:
        print "Enter the weight of the user in Kg's"
        # Get the input from the user and check it's of correct type
        try:        
            weight_of_the_user = float(raw_input())
            # isintance will check the type of the input and returns true/false
            if isinstance(weight_of_the_user,float):
                break 
        #If user inputs wrong type then the except will run
        except ValueError:
            print 'The value you have enteed is not a float value.Please enter the input in float value and in kilograms'  
        
    # Get the height of the user through keyboard
    while True:
        print "Enter the height of the user in Kg's"
        try:        
            height_of_the_user = float(raw_input())
            if isinstance(height_of_the_user,float):
                break 
        except ValueError:
            print 'The value you have enteed is not a float value.Please enter the input in float value and in meters'  
        
    # Creating an object for a class
    
    bmi_calculator_object = bmiCalculator(weight_of_the_user,height_of_the_user)
    
    # This method calculates BMI of the user
    bmi_calculator_object.calculate_bmi()

    # This method is used to calculate the user's category
    bmi_calculator_object.check_user_bmi_category()

    # This method is used to read the text file and compare the BMI value
    bmi_calculator_object.read_csv_file()

if __name__ == "__main__":
    get_input_to_calcluate_bmi()


