# User defined functions - code instructions that YOU write/ create.

# How to write a function
# part 1- function definition
# () --> round brackets/ parameters
def welcome_message():
    print('hello good morning.') 

# part 2 - function invocation/ call
welcome_message()

def calculate(num1):    
    # num1 = int(input("please type in a number: "))
    num1 += 10
    print(num1)

calculate(10)

# practice
def foodOrder():
    print('hamburger, chicken sandwich, salad')
    order = input("what would you like to order?")
    print(order)

foodOrder()

# Parameters and Arguments

# Parameters and arguments are data that can be passed inside
# of a function to follow instructions. 

# num1 and num2 are parameters. these are placeholders for data.
#P= parameter == P= placeholder

# this placeholder data is not REAL. it is intended to be a 
# reserve for actual incoming data.
# this is used in the function definition. 

def findAvg(num1, num2):
    print(num1 +num2)

# Arguments are REAL data in the function call
# There must be the same number of arguments as there are parameters
# otherwise you will get an error. 
# Argument == real data --> in court to make a argument you 
# need facts

findAvg(10,9)

