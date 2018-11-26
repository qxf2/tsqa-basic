"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
Changes in the program
    # Passing more number of arguments

"""
# Passing two arguments in the function
# No need to worry about what is argument here
# This called function will get execute for three different set of values
def fizz_buzz(mod3Value,mod5Value=30):
   "Fizz buzz program-Default arguments"
   if mod3Value % 3 == 0 and mod5Value % 5 == 0:
       print 'Fizz Buzz'
   elif  mod3Value % 3 == 0:
       print 'Fizz'
   elif mod5Value % 5 == 0:
       print 'Buzz' 

# Program starts here 
if __name__ == "__main__":
    # Passing only mod3value in the calling function
    fizz_buzz(33)
    # Passing mod3value and mod5value in the calling function
    fizz_buzz(34,mod5Value=65)
    # Passing values without variable names
    fizz_buzz(22,35)
