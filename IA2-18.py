"""
We will use this script to learn Python:Concepts of _Class and Objects in BMI Calculator.
The script is an example of BMI_Calculator implemented in Python using methods and constructor.
The BMI_Calculator:
    # Get the weight(Kg) of the user
    # Get the height(m) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in meters*height in meters


        """
class BMI_Calculator:
    pass

    #class variable
    BMI = 'calculator'

    #The init constructor for weight & height
    def __int__(self,weight,height):

        #instance variable
        self.weight = weight
        self.height = height


    #another instance constructor for weight & height
    def calculate_BMI(self):
        return (round((self.weight/self.height)**2),2)


weight = float(input("Enter the weight in kg:"))
height = float(input("Enter the height in meters:"))

   #object instant
file = BMI_Calculator(weight, height)
print("The BMI of the user is: ", file.calculate_BMI(), "kg/sq.metre")
# inputs for the weight & height of the user


if  BMI_Calculator< 18.5:
    print("Oh No!!! UnderWeight")
    print("The Ideal BMI Range is : 18.5 to 25 ")
    Gain_Weight = round((18.5 * weight * height - weight), 2)
    print("Weight to be Gained to Reach the Ideal BMI is:", Gain_Weight, "Kg")

elif BMI_Calculator >= 18.5 and BMI_Calculator <= 25:
    print("Hurrayyy!!! NormalWeight")
    print("The Ideal BMI Range is : 18.5 to 25")
    print("Good Keep It Up")

elif BMI_Calculator > 25 and BMI_Calculator <= 29.99:
    print("Ohhh!!! OverWeight")
    print("The Ideal BMI Range is : 18.5 to 25")
    Reduce_Weight = round((weight - height * height * 25), 2)
    print("Weight to be Reduced to Reach the Ideal BMI is :", Reduce_Weight,"Kg")

elif BMI_Calculator >= 30:
    print("{face screaming in fear}")
    print("The Ideal BMI Range is : 18.5 to 25")
    Reduce_Weight = round((weight - height * height * 25), 2)
    print("Weight to be Reduced to Reach the Ideal BMI is :{1}", Reduce_Weight, "Kg")