"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
Changes in the program
    # String initialization
    # Printing fizz buzz values with string
New terminologies
    # String and string operations
"""


# Empty list initialization
list_no_zero_reminders = []
# String inititalization
string_1 = "sample"  
for each_value in range(101):
    if each_value % 3 == 0 and each_value % 5 == 0:
        # Concatinating the string value with fizz buzz
        print string_1 + 'Fizz Buzz'
    elif each_value % 3 == 0:
        print string_1 + 'Fizz'
    elif each_value % 5 == 0:
        print string_1 + 'Buzz'
    else:
        # List append operations
        list_no_zero_reminders.append(each_value)
print list_no_zero_reminders   

