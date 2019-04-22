"""
We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters

Exercise 4:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user comes
        in underweight ,normal weight or obesity. Read the CSV which contains player data and compare a user BMI 
        with a player.Create functions for calculating BMI and check the user category.       
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
            ii)Create a function to calculate BMi
            iii)Create one more function for checking user category
            iv)Create a function to read the CSV file and return the matched player

"""

import os

def get_input_to_calcluate_bmi():
    "This function gets the input from the user"  
    print("Enter the weight of the user in Kg's")
    # Get the weight of the user through keyboard
    weight_of_the_user = input()

    # Get the height of the user through keyboard
    print("Enter the height of the user in meters")
    height_of_the_user = input()

    return weight_of_the_user,height_of_the_user

def calculate_bmi(weight_of_the_user,height_of_the_user):
    "This function calculates the bmi"
    # Calculate the BMI of the user according to height and weight
    bmi_of_the_user = round(weight_of_the_user/(height_of_the_user * height_of_the_user),1)
   
    # Return the BMI of the user to the called function
    return bmi_of_the_user

def check_user_bmi_category(bmi):
    "This function checks if the user is underweight, normal, overweight or obese"    
    if bmi <= 18.5:
         print("The user is considered as underweight")
    elif bmi > 18.5 and bmi < 24.9:
         print("The user is considered as normal weight")
    elif bmi > 25 and bmi <= 29.9:
        print("The user is considered as overweight")
    elif bmi >=30:
        print("The user is considered as obese")
    
def compare_user_bmi_with_player_csv(bmi_value):
    "This functions reads the CSV file and compare the BMI value with players and returns the players name"
    # To read the CSV file we have to join the path where it's located   
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data',"all_players_data.csv"))
    matched_player = []

    # To open the text file and assign to object fp
    with open(filename,"r") as fp:
        all_lines = fp.readlines()              
        for each_line in all_lines:            
            # Fetch the player name from the file           
            player_name = each_line.split(',')[0]                       
            # Fetch the player BMI from the file          
            player_bmi = each_line.split(',')[-1].split('\n')[0]            
            # Checks player BMI and user BMI are equal 
            if float(player_bmi) == bmi_value:
                matched_player.append({player_name:player_bmi})
                         
        if not matched_player:
            print("Your BMI is not matching with any of the players dataset which is used here")
        else:
            print("Your BMI is matching with")
            print matched_player 
       
# Program starts here
if __name__ == "__main__":
    # This calling function gets the input from the user
    weight_of_the_user,height_of_the_user = get_input_to_calcluate_bmi()     
    
    # This calling function calculates the BMI of the user
    bmi_value = calculate_bmi(weight_of_the_user,height_of_the_user)
    print("BMI of the user is :", bmi_value)

    # This function is used to calculate the user's criteria
    check_user_bmi_category(bmi_value)

    # This function is used to read the csv file and compare the BMI value
    compare_user_bmi_with_player_csv(bmi_value)