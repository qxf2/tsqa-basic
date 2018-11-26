"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
Changes in the program
    # Using range functions 
    # Appending the values in the new list which are not divided by 3 and 5
New terminologies
    # Empty list initialization
    # Append function
"""
# Hope you remember what is range and you would have google it already
# If not do it now
list_range_numbers = range(100)
# Intializing empty list here
# Still if you are so much eager to learn about list google it
list_no_zero_reminders = []  
for each_value in list_range_numbers:
    if each_value % 3 == 0 and each_value % 5 == 0:
        print 'Fizz Buzz'
    elif each_value % 3 == 0:
        print 'Fizz'
    elif each_value % 5 == 0:
        print 'Buzz'
    else:
        # append is the list operation and we can explain you later
        list_no_zero_reminders.append(each_value)
print list_no_zero_reminders

