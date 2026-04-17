# Create a coin machine function that takes in different dollar bill amounts
# and outputs the correct change amount in quarters.

# Your program should take in the following bill 
# amounts as a input; 1s, 5s, 10s, and 20s. your coin machine should print
# out the correct change in quarters (ex. 1 dollar should return 4 quarters)
# if the machine recieved a bill amount that is not listed, your function
# should print out, bill amount rejected. 

# keyword 
# coin machine - take in bills, returns quarters
# function - we need to make a function


def coinMachine():
    billAmount = int(input("Please insert a bill in the following amounts: 1, 5, 10, 20 "))   
    if billAmount == 1:
        print("dispencing 4 quarters.")
    elif billAmount == 5:
        print("dispencing 20 quarters.")
    elif billAmount == 10:
        print("dispencing 40 quarters.")
    elif billAmount == 20:
        print("dispencing 80 quarters.")
    else:
        print("Sorry, this bill amount is not accepted.")

# coinMachine()


# Create a college acceptance function. Your function 
# should take in the data as parameters. 
# Your function needs to check if the user has over a 3.5 GPA.
# if their GPA is greater or equal to 3.5, they will be given 
# an offer. else, they will need to get their grade up and apply again. 
 
# function + parameter
# greater or equal >=
# 3.5 float represents gpa
# if; its greater than 3.5 tell them they get offer
# else; tell them they need to re-apply

# create an elif condition where if the student has a 2.8 or higher gpa
# they can get a conditional offer.
 
def collegeOffer(gpa):
    if gpa >= 3.5:
        print("Congrats you have been given an offer to our school.")
    elif gpa >= 2.8:
        print("Congrats you have been given a conditional offer to our school.")
    else:
        print("Unfortunately, you have not been accepted.")

collegeOffer(3.0)