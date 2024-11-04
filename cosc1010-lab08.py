# Quinn Kwiatkowski
# UWYO COSC 1010
# Submission Date: 11/10/2024
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to: None

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convertString(string):
    try:
        integer = int(string)
        return integer
    except ValueError:
        if string.count('.') == 1: # Make sure that there is only one decimal place
            try:
                float = float(string)
            except ValueError:
                return False
        return False

userInput = input("Enter a number: ")

output = convertString(userInput)
if output is False:
    print("Could not convert to string or float, womp womp.")
else:
    print("Converted string:", output)

print("*" * 75)
# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slopeIntercept(m, lowerX, upperX, b):
    y = [(m*x)+b for x in range(lowerX,upperX+1)]
    return y

while True:
    # Taking all the inputs from the user, and breaking the program if the user types 'exit'
    mInput = input("Enter a m value, or 'exit' to exit: ")
    if mInput.lower() == 'exit':
        break
    lowerXInput = input("Enter a lower x value, or 'exit' to exit: ")
    if lowerXInput.lower() == 'exit':
        break
    upperXInput = input("Enter an upper x value, or 'exit' to exit: ")
    if upperXInput.lower() == 'exit':
        break
    bInput = input("Enter a b value, or 'exit' to exit: ")
    if bInput.lower() == 'exit':
        break

    # Convert to string using the function from the first problem:
    m = convertString(mInput)
    lowerX = convertString(lowerXInput)
    upperX = convertString(upperXInput)
    b = convertString(bInput)

    if m is None or lowerX is None or upperX is None or b is None:
        print("Enter numbers!")
        continue

    result = slopeIntercept(m,lowerX,upperX,b)
    if result is False:
        print("Invalid entry, try again.")
    else:
        print("y values are: ", result)

print("*" * 75)
# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quadratic(a, b, c):
    # Solving for the roots of the quadratic equation
    squareRoot = ((b**2)-4*a*c)**(1//2)
    if squareRoot < 0:
        return null
    x1 = (-b+squareRoot)/(2*a)
    x2 = (-b-squareRoot)/(2*a)
    return x1, x2

while True:
    # Takes an input from the user for the a, b, and c values of the quadratic
    aInput = input("Enter a value for a, or 'exit' to exit: ")
    if aInput.lower() == 'exit':
        break
    bInput = input("Enter a value for b, or 'exit' to exit: ")
    if bInput.lower() == 'exit':
        break
    cInput = input("Enter a value for c, or 'exit' to exit: ")
    if cInput.lower() == 'exit':
        break

    # Convert to string using the function from the first problem
    a = convertString(aInput)
    b = convertString(bInput)
    c = convertString(cInput)

    result = quadratic(a, b, c)

    print("The roots for the function are: ", result)
