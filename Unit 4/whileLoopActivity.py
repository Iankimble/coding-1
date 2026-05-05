saveings = 0
goal = 1000

# while saveings < goal:
#     print("you currently have:" + str(saveings))
#     deposit = int(input("how much do you want to add ?"))
#     saveings += deposit
#     print("you have  " + str(saveings) + " in your account")
#     if saveings >= goal:
#         print("congrats! you have enough for your trip")
#     else:
#         print("keep saving.")


# Create a function that takes in a user password and 
# checks if it is correct. If The password is correct, the user 
# should get a message saying "congrats, you have access".
# Else, the program should tell them to try again. Your program
# should have a WHILE loop that will repeat asking the user to type
# in their password IF they get it wrong. 

# we need to create a function
# if pw correct grant access while loop stops / 
# else - continue to ask user for correct pw

def pwLoop():
    pw = '1234abcd'
    userPw= input(" What is your password? ")
    
    while pw != userPw:
        print(" please try again")
        userPw= input(" What is your password? ")
        if pw == userPw:
            print('congrats')
pwLoop()