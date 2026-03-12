# 1. What is the difference between a function 
# parameter and a function argument?
" parameters are placeholders for data in the function definition."
" arguements are real data that runs in the function call."


# 2. Create a function that will display the number of books a user
# read in 1 year and also print out the title of their favorite book.
# your function should take two parameters; the number of books they 
# read,and the title of their favorite book. 
# When your progam runs, your result should look like this:

"I read 10 books this year"
"My favorite book was We Refuse by Kellie Carter Jackson"

# hint you will need to use a built-in 
# function for changing data types

def bookChallenge(numOfBooks, titleOfFav):
    print("I read " + str(numOfBooks) +" books this year")
    print("My favorite book was" + titleOfFav)

bookChallenge(390, " the pearl")

# 3. What do the following error messages mean? Please write your 
# responses as a string data type
"syntax error - means that we broke the grammar rules. "
"wrote something wrong. wrote something the computer "
"doesnt understand"

"name error - this means the computer cant find a variable"
" or function name becuse it was not defined/ the "
"computer was not told what it means"

# 4. Create a function calculates a number. The number should
# be passed into your function using the input() function. 
# your function should do the following:
# multiply the number by itself, 
# then divide that number by 2, then add 5
# then print the result. 

def calculate():
    number  = int(input("please type in a number: "))
    sum = number * number /2 + 5
    print(sum)

calculate()