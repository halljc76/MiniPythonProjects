# import matplotlib.pyplot as plt
# import numpy as np
import random
import math 

"""
June 8th Update:
Working to add matplotlib graph to show statistical distribution of the area being computed 30+ times, per CLT.
"""

def function(reference, x):
    functions = {1: x, 2: x**2, 3: x**3, 4: 1/x, 5: math.sin(x), 6: math.cos(x)}
    for key in functions.keys():
        if key == reference:
            return functions[key]
            
def limits(reference):
    if reference == 4:
        integerLimits = [i for i in range(1,51)]
    else:
        integerLimits = [i for i in range(0,51)]
    irrationalLimits = [math.pi, math.e]
    limitChosen = False

    while not limitChosen:
        lower_choice = input("Please input '1' for an integer limit or '2' for an irrational limit.")
        try:
            lower_choice = int(lower_choice)

        except TypeError or lower_choice not in [1,2]:
            lower_choice = input("Please input '1' for an integer limit or '2' for an irrational limit.")

        if lower_choice not in [1,2]:
           print(limitChosen)
           print("Invalid choice.")
        
        else:
            limitChosen = True
        
    if int(lower_choice) == 1:
        try:
            if reference == 4:
                lower = int(input("Please input an integer 1-50, inclusive."))
            else:
                lower = int(input("Please input an integer 0-50, inclusive."))
        except int(lower) not in integerLimits or TypeError:
            print("Invalid lower limit.")
            lower = int(input("Please input an integer 0-50, inclusive."))
    else:
        try:
            lower = input("Please input 'pi' or 'e' for your irrational limit.")
            if lower == 'pi':
                lower = math.pi
            elif lower == 'e':
                lower = math.e
        except lower not in irrationalLimits or TypeError:
            print("Invalid lower limit.")
            lower = int(input("Please input 'pi' or 'e' for your irrational limit."))

    limitChosen = False
    

    while not limitChosen:
        upper_choice = input("Please input '1' for an integer limit or '2' for an irrational limit.")
        try:
            upper_choice = int(upper_choice)
            limitChosen = True
        except TypeError:
            upper_choice = input("Please input '1' for an integer limit or '2' for an irrational limit.")

        if upper_choice not in [1,2]:
            print("Invalid choice.")
    
    if int(upper_choice) == 1:
        try:
            if reference == 4:
                upper = int(input("Please input an integer 1-50, inclusive."))
            else:
                upper = int(input("Please input an integer 0-50, inclusive."))
        except int(upper) not in integerLimits or TypeError:
            print("Invalid upper limit.")
            lower = int(input("Please input an integer 0-50, inclusive."))
    else:
        try:
            upper = input("Please input 'pi' or 'e' for your irrational limit.")
            if upper == 'pi':
                upper = math.pi
            elif upper == 'e':
                upper = math.e
        except upper not in irrationalLimits or TypeError:
            print("Invalid upper limit.")
            lower = int(input("Please input 'pi' or 'e' for your irrational limit."))
    return lower, upper

def integration(reference, lower, upper, numPoints):
    integral = 0.0
    randomVals = [] 
    for i in range(numPoints):
        randomVals.append(random.uniform(lower, upper))

    for value in randomVals:
        integral += function(reference, value)
    
    area = ((upper - lower) / float(numPoints)) * integral 
    return area

def main():
    print("Basic Monte-Carlo Integration Program:")
    print("This program heuristically uses 1000 points to statistically estimate the value of an integral of an elementary function.")

    print("Functions: ")
    print("'1' --> Linear")
    print("'2' --> Quadratic")
    print("'3' --> Cubic")
    print("'4' --> Rational (1/x)")
    print("'5' --> Sine")
    print("'6' --> Cosine")

    stringFunctions = {1: "x", 2: "x**2", 3: "x**3", 4: "1/x", 5:"sin(x)", 6:"cos(x)"}

    choice = input("Choose a number 1-6, inclusive, according to which function you would like to use:")
    while choice not in ["1","2","3","4","5","6"]:
        choice = ("Choose a number 1-6, inclusive, according to which function you would like to use:")

    reference = int(choice)
    numPoints = 1000

    lower, upper = limits(reference)
    while (lower > upper):
        print("Your upper limit exceeded your lower limit. Let's choose the limits again.")
        lower, upper = limits()
    area = integration(reference, lower, upper, numPoints)
    print("The area from " + str(lower) + " to " + str(upper) + " of " + stringFunctions[reference] + " is " + str(area))

main()
