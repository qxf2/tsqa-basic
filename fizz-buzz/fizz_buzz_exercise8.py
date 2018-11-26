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
    # Classes,self,method
"""

# Defining the class here with class keywords
# Don't worry about what is class
class fizzBuzz1:
    "Fizzbuzz program with class examples"
    # This is the method we used to implement fizz program
    def method_inside_class(self,mod5Value,mod3Value):
        "Fizz buzz program-implemented here"
        if mod3Value % 3 == 0 and mod5Value % 5 == 0:
            print 'Fizz Buzz'
        elif mod3Value % 3 == 0:
            print 'Fizz'
        elif mod5Value % 5 == 0:
            print 'Buzz'

#Program starts here
if __name__ == "__main__":
    # Creating an object
    # As of now let's leave what is class and object
    class_object = fizzBuzz1()
    # Calling the method which is inside the class using '.'
    class_object.method_inside_class(45,77)
  
