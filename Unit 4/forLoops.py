# a FOR loop is a type of looping contstruct that repeats code 
# instruction a specficic (finite) amount of times. 

# For loop syntax
for x in range(0,10,2):
    print('x = '+ str(x))
# range() function is a special function that lets us count
# sequentially upto a certain number, even at certain intervals.


# For loops work really nicely with collections such as list, because
# we may want to do something to each piece of data in a list

coworkers = ['Bill','Mary','Philip']

# for worker in coworkers:
#     print(worker + ' has gotten a gift card. ')


for worker in coworkers:
    if worker == 'Mary':
        coworkers.remove('Mary')
        print(coworkers)
    
prices= [10.00, 20.00, 40.00]

for item in prices:
    discount = 5.00
    item -= discount
    print(item)