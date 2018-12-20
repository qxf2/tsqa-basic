"""
We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters

Exercise 3:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user 
        comes in underweight ,normal weight or obesity. Create functions for calculating BMI and 
        check the user category.
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
            i)Create a function to get the input
            ii)Create one more function to calculate BMi
            iii)Create one more function for checking user category

"""

def get_input_to_calcluate_bmi():
    "This function gets the input from the user"    
    print("Enter the weight of the user in Kgs")    
    # Get the weight of the user through keyboard
    weight_of_the_user = input()

    # Get the height of the user through keyboard
    print("Enter the height of the user in meters")
    height_of_the_user = input()

    return weight_of_the_user,height_of_the_user

def calculate_bmi(weight_of_the_user,height_of_the_user):
    "This function calculates the BMI"
    # Calculate the BMI of the user according to height and weight
    bmi_of_the_user = weight_of_the_user/(height_of_the_user * height_of_the_user)    

    # Return the BMI of the user to the called function
    return bmi_of_the_user

def check_user_bmi_category(bmi):
    "This function checks whether the user comes under under weight, normal or obesity"    
    if bmi <= 18.5:
         print("The user is considered as underweight")
    elif bmi > 18.5 and bmi < 24.9:
         print("The user is considered as normal weight")
    elif bmi > 25 and bmi <= 29.9:
        print("The user is considered as overweight")
    elif bmi >=30:
        print("The user is considered as obese")
    
# Program starts here
if __name__ == "__main__":    
    # This calling function gets the input from the user
    weight_of_the_user,height_of_the_user = get_input_to_calcluate_bmi()

    # This calling function stores the BMI of the user
    bmi_value = calculate_bmi(weight_of_the_user,height_of_the_user)

    print("BMI of the user is :",bmi_value)

    # This function is used to calculate the user's criteria
    check_user_bmi_category(bmi_value)