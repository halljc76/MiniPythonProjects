import matplotlib.pyplot as plt
import numpy as np
from random import uniform
from math import sin, cos, pi, e


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
    resetLimitChosen = False
    upperString = ''
    lowerString = ''

    while not limitChosen:
        lower_choice = input("Please input '1' for an integer limit or '2' for an irrational limit.")
        try:
            lower_choice = int(lower_choice)

        except TypeError or lower_choice not in [1,2]:
            lower_choice = input("Please input '1' for an integer limit or '2' for an irrational limit.")

        if lower_choice not in [1,2]:
            print("Invalid choice.")
        
        else:
            limitChosen = True
        
    while limitChosen:
        if int(lower_choice) == 1:
            try:
                if reference == 4:
                    lower = int(input("Please input an integer 1-50, inclusive."))
                else:
                    lower = int(input("Please input an integer 0-50, inclusive."))
            except int(lower) not in integerLimits or TypeError:
                print("Invalid lower limit.")
                lower = int(input("Please input an integer 0-50, inclusive."))
            
            limitChosen = resetLimitChosen
            lowerString = '$' + str(lower) + '$'
        else:
            try:
                irrational = input("Please input 'pi' or 'e' in your limit.")
                lower = input("Please input a factor for this limit (integer).")
                try:
                    lower = int(lower)
                except int(lower) not in integerLimits or TypeError:
                    print("Invalid factor for the irrational limit.")
                    lower = input("Please input a factor for this limit (integer).")
                integer = lower
                lower = float(lower)

                if irrational == 'pi':
                    lower = lower * irrationalLimits[0]
                    lowerString = '$' + str(integer) + 'pi$'
                    limitChosen = resetLimitChosen
                elif irrational == 'e':
                    lower = lower * irrationalLimits[1]
                    lowerString = '$' + str(integer) + 'e$'
                    limitChosen = resetLimitChosen
            except irrational not in irrationalLimits or TypeError:
                print("Invalid lower limit.")
            
    while not limitChosen:
        upper_choice = input("Please input '1' for an integer limit or '2' for an irrational limit.")
        try:
            upper_choice = int(upper_choice)
            limitChosen = True
        except TypeError:
            upper_choice = input("Please input '1' for an integer limit or '2' for an irrational limit.")

        if upper_choice not in [1,2]:
            print("Invalid choice.")
    
    while limitChosen:
        if int(upper_choice) == 1:
            try:
                if reference == 4:
                    upper = int(input("Please input an integer 1-50, inclusive."))
                else:
                    upper = int(input("Please input an integer 0-50, inclusive."))
            except int(upper) not in integerLimits or TypeError:
                print("Invalid upper limit.")
                upper = int(input("Please input an integer 0-50, inclusive."))
            
            limitChosen = resetLimitChosen
            upperString = '$' + str(upper) + '$'
            
        else:
            try:
                irrational = input("Please input 'pi' or 'e' in your limit.")
                upper = input("Please input a factor for this limit (integer).")
                
                try:
                    upper = int(upper)
                except int(lower) not in integerLimits or TypeError:
                    print("Invalid factor for the irrational limit.")
                    upper = input("Please input a factor for this limit (integer).")
                integer = upper
                upper = float(upper)

                if irrational == 'pi':
                    upper = upper * math.pi
                    upperString = '$' + str(integer) + 'pi$'
                    
                    limitChosen = resetLimitChosen
                elif irrational == 'e':
                    upper = upper * math.e
                    upperString = '$' + str(integer) + 'e$'
                    limitChosen = resetLimitChosen

            except irrational not in irrationalLimits or TypeError:
                print("Invalid lower limit.")
            

    return lower, upper, lowerString, upperString

def integration(reference, lower, upper, numPoints):
    integral = 0.0
    randomVals = np.zeros(numPoints) 
    for i in range(numPoints):
        randomVals[i] = (random.uniform(lower, upper))

    for value in randomVals:
        integral += function(reference, value)
    
    area = ((upper - lower) / float(numPoints)) * integral 
    return area

def plot(stringFunctions, numPoints, lower, lowerString, upper, upperString, reference):
    areas = []

    for i in range(numPoints):
        areas.append(integration(reference, lower, upper, numPoints))
    
    plt.hist(areas, bins = int(math.sqrt(numPoints)), ec = 'black')
    plt.title("Distribution of Estimated Areas of " + stringFunctions[reference] + " from " + lowerString + " to " + upperString + ".")
    plt.xlabel("Area (units)")
    plt.ylabel("Number of Calculations Within Bin")
    plt.show()

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
    
    stringFunctions = {1: '$x$', 2: "$x^{2}$", 3: "$x^{3}$", 4: "$1/x$", 5:"$sin(x)$", 6:"$cos(x)$"}

    choice = input("Choose a number 1-6, inclusive, according to which function you would like to use:")
    while choice not in ["1","2","3","4","5","6"]:
        choice = ("Choose a number 1-6, inclusive, according to which function you would like to use:")

    reference = int(choice)
    numPoints = 1000

    lower, upper, lowerString, upperString = limits(reference)
    while (lower > upper):
        print("Your lower limit exceeded your upper limit. Let's choose the limits again.")
        lower, upper = limits(reference)
    
    plot(stringFunctions, numPoints, lower, lowerString, upper, upperString, reference)
    

if __name__ == '__main__':
    main()
