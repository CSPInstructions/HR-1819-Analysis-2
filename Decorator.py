# We define a function that doubles the outcome of a function
def double(function):
    # We define an internal function that takes an undefined amount of arguments
    def doubler(*values):
        # We return the result of the provided function multiplied by two
        return 2 * function(*values)
    # Now we return the doubler function
    return doubler

# We define a function that calculates the factorial of a number
def factorial(number):
    # We define a result variable that will accumalate the values
    result = 1

    # We loop over all the numbers from two, to the number provided in the parameters
    for currentNumber in range(2, number + 1):
        # We multiple the current result with the current number
        result = result * currentNumber

    # We return the result
    return result

# We tell Python that we want to use double as a decorator
# This means that double will be executed with decoratedFactorial as argument
@double
# We define the factorial function, decorated with double
def decoratedFactorial(number):
    # We define a result variable that will accumalate the values
    result = 1

    # We loop over all the numbers from two, to the number provided in the parameters
    for currentNumber in range(2, number + 1):
        # We multiple the current result with the current number
        result = result * currentNumber

    # We return the result
    return result

# We can accomplish the same decoration manually
# This is what happens when we use decorators
manualDecoratedFactorial = double(factorial)

# We print the result of the different functions
print(decoratedFactorial(5))
print(manualDecoratedFactorial(5))