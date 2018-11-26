"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
Changes in the program
    # Using classes
    # Accessing the funtion wth dot operator
New terminology
    # Classes,self,method,init
"""
# Class definition
class exampleSecond:
    "To explain the class program"
    # init method is called when the object is created
    def __init__(self,mod3Value=0,mod5Value=0):
        "Initializing the mod3 and mod5 values"
        self.mod3Value = mod3Value
        self.mod5Value = mod5Value
        
    def fizzBuzz_function(self):
        "Fizz buzz method implemented here"
        if self.mod5Value % 5 == 0 and self.mod3Value %3 == 0:
            print 'Fizz Buzz'
        elif self.mod5Value % 5 == 0:
           print 'Buzz'
        elif  self.mod3Value %3 == 0:
           print 'Fizz'

#Program starts here
if __name__ == "__main__":
    # Object creation
    class_object = exampleSecond(20,30)
    # Calling the method which is inside a class
    class_object.fizzBuzz_function()
