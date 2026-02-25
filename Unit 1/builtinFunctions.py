# built in functions= code instructions that are built-in
# to the programming language. usually locked away behind
# a keyword.
# print is a built in function that lets us printout data

# in the terminal.
print("Ian Kimble") 
print(2+2)

message = "this is a message that I wrote in Python."

print(message)

# input() is a built in function that allows us to 
# type in (put in) data through the termiinal. to use 
# input it must be ASSIGNED to a variable

#name = input("please type in your name: ")
#print(name)

# Data-casting Built in Functions (Data Conversion)
# Datacasting are functions that allow us to change data types

# str() - this built in function will change whatever is in the round brackets
# into a string.

number = 100
print(type(number)) # class int = integer
print(type(str(number))) # class str = string

# int() - this built in function will change whatever is in the round
# brackets into a integer (whole number)

number = "100"
print(type(number)) # class str = string
print(type(int(number))) # class int = integer

# float()