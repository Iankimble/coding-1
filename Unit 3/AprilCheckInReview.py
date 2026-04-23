# In codespaces, work on writing program code for 
# the following prompt. When done, copy and paste your program solution below.

# You've been tasked with creating a program that charges a fee based 
# on the number of eggs a user purchase.  Your program should take in the 
# number of eggs being purchases as an argument When a user passes in a number. 
# (the number of eggs being bought), the program should charge a fee of 1.15 per
#  egg (for ex. 1 egg= 1.15, 2 eggs = 2.30, 3 eggs= 3.45, etc.) 
# If 6 or more eggs are purchased the price of the egg is changed from 1.15
#  to 1.00 (ex. 6 = 6.00, 7 = 7.00, etc.)

# also, if the number of eggs is more than 12, the new price per 
# egg should be .75. 

# lastly, if a person is buying more than 20 eggs, inform the user 
# that they cannot buy that many eggs at 1 time. 

# We need to create a function that will determine the price of eggs
# based on how many eggs are being purchased
# > 6 egg = 1.15
# <= 6 eggs = 1.00
# <= 12 eggs = 0.75
# <= 20 egges = cant buy that many eggs 
# numbers of eggs is a argument

def eggPrice(eggCount):
    if eggCount < 6:
        total = eggCount * 1.15 