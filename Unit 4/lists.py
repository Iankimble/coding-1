# lists are a container data type for
# storing multiple types of data.

# lists are useful for keeping data, 
# organized, structured, and space-friendly

# list syntax
# to create a list, we start with a name,
# followed by the assingment operator, and
# then square brackets. Inside the brackets
# is where we put our data.

blCodeing = ["intro coding", "coding 2"," ap comp sci"] 
print(blCodeing)

# every item in a list is called an index.
# lists are organized sequentially by index position
# lists always start at zero

print(blCodeing[2])

# list methods are functions that work on lists
# remember: functions just mean code instructions.

# the append method allows us to add an item at the END of a list
blCodeing.append("cyber security")
print(blCodeing)

# the insert method allows us to add an item ANYWHERE in a list so long as we tell it which index to pass
# it in
blCodeing.insert(2,10)
print(blCodeing)
