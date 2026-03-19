# Conditional Logic - A special class of function that
# lets use run specific instructions based on specific 
# data

# we use the if and else keywords to run different 
# instructions

# Conditional syntax - how to write a conditional block

absences = 0

if absences == 0:
    print("you have a dress down day.") 
    # if is the condition we are looking for
else:
    print("you must come in uniform.")
    # else is our default/ exit. what we want to happen
    # if we CANT find the data we are looking for. 

creditsToPass = 30

currentCredits = int(input("how many credits do you have? "))

if currentCredits < creditsToPass:
    print('sorry you do not have enough credits')
else:
    print("congrats you are graduating this year")

schoolYear = input("What year of High School are you in? ")

if schoolYear == 'Freshman':
    print('you will be taking intro to high school')
elif schoolYear =='Sophmore':
    print('you have to take state testing')
elif schoolYear == 'Junior':
    print('you need an internship')
else:
    print('sorry this info does not apply to you.')