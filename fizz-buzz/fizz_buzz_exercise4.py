"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
Changes in the program
    # Using main function
    # Using function
    # Passing 100 in the function
New terminologies
    # def keyword
    # if __name__ == "__main__"

"""
# This is the function which is called from the main program
def fizz_buzz(passed_value):
   "Fizz buzz program-Required Arguments"
   if passed_value % 3 == 0 and passed_value % 5 == 0:
       print 'Fizz Buzz'
   elif passed_value % 3 == 0:
       print 'Fizz'
   elif passed_value % 5 == 0:
       print 'Buzz'
   else:
       print passed_value

# Program starts here
# Don't worry if you dont't understand why the program starts here
if __name__ == "__main__":  
  fizz_buzz(100) # Calling the fizz_buzz function