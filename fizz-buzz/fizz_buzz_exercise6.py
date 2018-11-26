"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
Changes in the program
    # Passing keyword arguments    
"""

# Don't worry if you don't know what is keyword arguments
def fizz_buzz(mod3Value,mod5Value,name='Function'):
    "Fizz buzz program-Keyword arguments"
    if mod3Value % 3 == 0 and mod5Value % 5 == 0:
       print 'Fizz Buzz'
    elif  mod3Value % 3 == 0:
       print 'Fizz'
    elif mod5Value % 5 == 0:
       print 'Buzz'
    else:
        print name
     

# Program starts here 
if __name__ == "__main__":
    # Passing values in different order in the calling function
    fizz_buzz(mod5Value=65,mod3Value=34)
    fizz_buzz(mod3Value=12,mod5Value=20)
    fizz_buzz(13,11,'I overwrite function')
 
