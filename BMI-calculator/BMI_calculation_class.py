"""
Exercise 3:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user comes
        in underweight ,normal weight or obesity by creating a class. Read the CSV files which contains player data and compare your BMI 
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
import csv
import os

class bmiCalculator:
    "This class calculates the BMI of the user"
    def __init__(self,weight_of_the_user,height_of_the_user):
        self.weight_of_the_user = weight_of_the_user
        self.height_of_the_user = height_of_the_user
        self.matched_player = []
    
    def calculate_bmi(self):
        "This function calculates the bmi"
        # Calculate the BMI of the user according to height and weight
        self.bmi_of_the_user = round(self.weight_of_the_user/(self.height_of_the_user * self.height_of_the_user),1)

        print 'BMI of the user is : ' , self.bmi_of_the_user

    def check_user_bmi_category(self):
        "This function checks whether the user comes under under weight, normal or obesity"    
        if self.bmi_of_the_user <= 18.5:
            print 'The user is considered as underweight'
        elif self.bmi_of_the_user > 18.5 and self.bmi_of_the_user < 24.9:
            print 'The user is considered as normal weight'
        elif self.bmi_of_the_user > 25 and self.bmi_of_the_user <= 29.9:
            print 'The user is considered as overweight'
        elif self.bmi_of_the_user >=30:
            print 'The user is considered as obese'
        else:
            print 'Check the input units. It should be in kg and meters'   

    def read_csv_file(self):
        "This functions reads the csv file and compare the BMI value with players and returns the players name"   
        filename = os.path.abspath(os.path.join('..','training',"all_players_data.csv")) 
        with open(filename,"r") as fp:
            csv_file = csv.reader(fp)
            next(csv_file)                 
            for i, row in enumerate(csv_file):
                bmi_value_in_row = row[3]            
                player_name = row[0]
                #matched_bmi_value = approx_value(player_name,bmi_value_in_row,bmi_value) 
                if float(bmi_value_in_row) == self.bmi_of_the_user:
                    self.matched_player.append({player_name:bmi_value_in_row})                       
                
            if not self.matched_player:
                print 'No matching data'
            else:
                print 'Your BMI is matching with'
                print self.matched_player 
       
