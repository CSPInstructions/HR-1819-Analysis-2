# We're going to define a recursive factorial function
# A recursive function is a function that calls itself
def factorial(number):
    # We check whether the number is smaller or equal to 1
    if number <= 1:
        # If it is, we return 1
        return 1
    # We return the current number multiplied by the result of this function, with number - 1 as argument
    # This will add a new stack frame (block of memory) and continues building the return
    return number * fac(number - 1)

# We print the result of the factorial function with the number 5
print(factorial(5))

# While executing this function, the return value will be build up.
# We start by 5 * fac(5 - 1)
# Followed by 5 * 4 * fac(4 - 1)
# Followed by 5 * 4 * 3 * fac(3 - 1)
# Followed by 5 * 4 * 3 * 2 * fac(2 - 1)
# The number parameter has reached 1, which means that 1 will be returned as final result value
# Followed by 5 * 4 * 3 * 2 * 1