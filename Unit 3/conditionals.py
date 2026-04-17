# Conditionals statements - A construct that allows
# the program to make decisions based on the input data.

# We use the IF and ELSE Keywords to control 
# our decisions and outcomes.

# hasUmbrella = input("Its going to rain, do you have an umbrella") 

# if hasUmbrella == "yes":
#     print("Excellent. you will be dry in the rain.")
# else:
#     print("You are going to get your clothes wet in the rain.")

# sneakerCount = int(input("how many shoes do you have in stock?"))
 
# if sneakerCount < 10:
#     print("inventory is low, please order more shoes")
# else: 
#     print("sell as a many sneakers as you can.")


def userLogin():
    pw = int(input("what is the password?"))
    storedPw = 123
    if pw == storedPw: 
        print("congrats you have access")
    else:
        print("sorry access revoked")

# userLogin()

# in many cases, we want our programs to provide multiple outcomes
# based on the data recieved. 

# The ELIF keyword, allows use to make many more conditions that
# can give us more outcomes

def movieSelection():
    print("Here are all the movie genres we have: ")
    print('1: horror','2: sci-fi','3: romance','4: action')
    select = int(input('Please enter a number for a genre. ')) # always comes in as a string
    if select == 1: # "1" == 1 False
        print("Friday the 13th")
    elif select == 2: 
        print("The Matrix") 
    elif select == 3:
        print("The Notebook")
    elif select == 4:
        print('The Avengers')
    else: 
        print("Sorry, we didnt recognize your input.")

movieSelection()

# You have been tasked with creating a roller coaster admission function. 
# Your program should check the user's height and inform them if they are able
#  to ride the roller coaster. Your proram should take the user's height in 
# as a parameter. If they are over 5, they can get on th roller coaster. 
# Othrwise they should get a message saying they are too small to ride. 

def rollerCoasterAdmissionCheck()