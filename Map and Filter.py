# We define a pretty list printer, this prints the indexes and the values in a pretty manner
def prettyListPrinter(someList):
    # We print a line
    print("---------------------")

    # We loop through the items of the list
    for item in range(len(someList)):
        # We print the index with it's assigned value
        print("{0} => {1}".format(str(item), str(someList[item])))

    # We print another line
    print("---------------------")

# We define the map function. The map function takes in a list, does something to each item,
# and return a list with the updates values
def map(originalList, function):
    # Create the new list
    newList = []

    # Loop throught the items of the original list
    for item in originalList:
        # Execute the provided function with the current item as argument
        # Save the return value in the new list
        newList.append( function(item) )

    # Return the new list
    return newList

# We define the map function the way it's done during the analysis course
def analysisMap(originalList, function):
    # We return a list of all updates values from the orginal list
    return list(function(item) for item in originalList)

# We define the filter function. The filter function takes in a list,
# and returns a list of items that meet a certain condition
def filter(originalList, predicate):
    # We define the new list
    newList = []

    # We loop through the items in the original list
    for item in originalList:
        # We check whether the current items meets the condition
        if ( predicate(item) ):
            # If it does, we store the item in the new list.
            newList.append(item)

    # We return the list containing all the items that meet the condition
    return newList

# We define the filter function the way it's done during the analysis course
def analysisFilter(originalList, predicate):
    # We return a list of values from the orginal list that meet the condition
    return list(item for item in originalList if predicate(item))

# We're going to create some lambda functions that will be used for map and filter
# A lambda function is a function without a name. It's defined like below.
# A lambda function always returns the result
# Using lambdas allows us to make functions more adaptable to certain situations
mapFunction = lambda listItem: listItem * 2
secondMapFunction = lambda listItem: listItem / 2
filterFunction = lambda listItem: listItem % 2 == 0
secondFilterFunction = lambda listItem: listItem % 2 != 0

# We define a list of number
numberList = [1, 2, 3, 4, 5]

# We print the result of the two map functions
prettyListPrinter(map(numberList, mapFunction))
prettyListPrinter(analysisMap(numberList, secondMapFunction))

# We print the result of the two filter functions
prettyListPrinter(filter(numberList, filterFunction))
prettyListPrinter(analysisFilter(numberList, secondFilterFunction))