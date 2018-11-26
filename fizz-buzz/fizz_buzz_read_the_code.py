"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
"""
# Google for rang in python and see what it does
for each_value in range(1,100):
    # % or modulo gives the reminder
    if each_value % 3 == 0 and each_value % 5 == 0:        
        print (each_value,'Fizz Buzz')
    elif each_value % 3 == 0:
        print (each_value,'Fizz')
    elif each_value % 5 == 0:
        print (each_value,'Buzz')
   