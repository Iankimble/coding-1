# WHILE loop - code instructions that will run infinitely under specific
# conditions, unless the condition changes. 

secruityCheck = 0

while secruityCheck < 1:
    print("CAMERA IS MONITORING...") 
    secruityCheck= int(input("how many people are at the door?"))
    if secruityCheck >= 1:
        print("sound the alarm")
    