#ٍSaif Eldeen Soliman Abdeen Soliman 18102012
from py_expression_eval import Parser
import sympy as sp
import math
parser = Parser() #Parser is the main class of the library that contains the methods to parse, evaluate and simplify mathematical expressions

#pyexperssion eval is a Mathematical Expression Evaluator
#downloaded from github https://github.com/axiacore/py-expression-eval


eqn = input("Please enter the equation: ")
interval1 = float(input("Please enter the first Interval: "))
interval2 = float(input("Please enter the second Interval: "))
H = float(input("Please enter the vale of H: "))
b_A_over2 = (interval2 - interval1) /2 #b-a /2
AandB_over2 = (interval1 + interval2) /2 #a+b /2
fOfA = parser.parse(eqn).evaluate({'x' : interval1})
fOfB = parser.parse(eqn).evaluate({'x' : interval2})


midPoint = (interval2 - interval1) * parser.parse(eqn).evaluate({'x' : AandB_over2})

i=0
var1 = interval1 + H #divide the line into interavals with respect to H
tempX1 = (interval1 + var1) / 2 #the mid point of the new 2 intervals
compositeMid = 0 #will add the evaluated x in it (summation of mid points)

print("\n\n==================== MidPoint ====================\n")
print("The MidPoint is: ", midPoint)
while i < interval2:

    x = parser.parse(eqn).evaluate({'x' : tempX1})
    compositeMid += x

    print("X = ", tempX1, " F(X) = ", x)

    var1 += H
    tempX1 += H
    

    i = i + H 

print("The Midpoint Composite is: ", H*compositeMid)

#trapezodial
print("\n\n==================== Trapezodial ====================\n")

trapezodial = (interval2 - interval1) * ((fOfA + fOfB) / 2)

print("The Trapezodial is: ", trapezodial)

j=0
var2 = interval1
sumOfBetweenIntervals = 0
while j <= interval2:
    xi = parser.parse(eqn).evaluate({'x' : var2})

    print("X = ", var2, " F(X) = ", xi)

    if var2 != interval1 and var2 != interval2:
        sumOfBetweenIntervals += xi

    var2 += H
    j = j + H

trapComposite = (H / 2) * (fOfA + 2*sumOfBetweenIntervals + fOfB)

print("The Trapezodial Composite is: ",trapComposite)

#simpson
print("\n\n==================== Simpson ====================\n")

simpson = ((interval2 - interval1) / 6) * (fOfA +  4*parser.parse(eqn).evaluate({'x' : AandB_over2}) + fOfB)
print("The Simpson is: ",simpson)

k=0
z = 4
var3 = interval1 + H
summation = fOfA + fOfB
print("X = ", interval1, " F(X) = ", fOfA)
while var3 < interval2:
    xi = parser.parse(eqn).evaluate({'x' : var3})
    print("X = ", var3, " F(X) = ", xi)
    xi *= z
    if z == 4:
        z=2
    else:
        z=4

    

    summation += xi
    var3 += H
   # k = k + H

simpsonCompiste = (H/3) * summation
print("X = ", interval2, " F(X) = ", fOfB)

print("The Simpson Composite is: ", simpsonCompiste)