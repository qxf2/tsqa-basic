"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
Changes in the program
    # Using return
New terminology
    # Return
"""

def fizz_buzz(value):
    "Fizz buzz program-Function return"
    if value % 3 == 0 and value % 5 == 0:
        # I am returning the value to the calling function
        return 'Fizz Buzz'
    elif  value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz' 
    else:
        return  'I am returning the function value'

# Program starts here
if __name__ == "__main__":
    # The returned value from the called function is getting stored in the my_output
    my_output = fizz_buzz(value=17)
    # The returned value is getting printed here    
    print my_output


    