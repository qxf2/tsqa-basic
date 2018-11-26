"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python
The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
Changes in the program
    # Using files    
New terminology
    # write,readline,with open,as
"""
# You may notice new words and new way of implementing fizz buzz program
# You don't need to worry if you don't understand anything here

def fizzbuzz(max_num):
    "This method implements FizzBuzz by writing and reading the values from the file"
    # Here I write the value to the file 'myfile.txt    
    with open('myfile.txt','w') as fp:
        fp.write(str(3)+"\n")
        fp.write(str(5))

    # Here I read the myfile.txt and store the values in num1 and num2
    with open('myfile.txt','r') as f:
        num1 = int(f.readline())  
        num2 = int(f.readline())
    
    # for loop is looped until it reaches the max_num
    for values in range(1,max_num):
        if values%num1==0 and values%num2==0:
            print(values,'Fizz Buzz')
        elif values%num1==0:
            print(values,'Fizz')
        elif values%num2==0:
            print(values,'Buzz')

#Program starts here
if __name__=='__main__':
    fizzbuzz(100)