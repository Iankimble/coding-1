#1. Convert the following into an interger and print the result 
age = "16"

print(type("16")) # --> this will give ... str 
# type = shows you what data type that thing is

print(int(age)) # int() --> anything passed in here will transform into a integer

#2. Convert the following into an string and print the result
score = 85
print(str(score)) # --> anything passed in here will transform into a string

#3. Convert the following into an float and print the result
price = 19.99

# Already a float - does not need to be convert

#4. Convert the following variables into integers and then multiply them together
# and print the result. 
num1 = input("Enter a number: ") # anything passed in here automatically becomes
# a string
num2 = input("Enter another number: ")

print('this is the first number we typed ' + num1)
print('here is the second number we typed ' + num2)

print(int(num1) * int(num2)) # int  * int

#5. Fix the following code block

print('It will cost ' + str(120.00) + ' dollars to to get everyone lunch.' )


#6. Fix the following code block - result should be 104
print(int("100") + 4)

