"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
Changes in the program
    # We are intializing the list
    # We are looping the list here
New terminiologies 
    # List intialization
"""
# Intializing the list with the name of values
# We will teach list later,Just read the code and understand
values = [1,2,5,6,90,33,45]
for each_value in values:
    if each_value % 3 == 0 and each_value % 5 == 0:
        print 'Fizz Buzz'
    elif each_value % 3 == 0:
        print 'Fizz'
    elif each_value % 5 == 0:
        print 'Buzz'
    else:
        print each_value
