# -*- coding: utf-8 -*-

# Write a program that does the following in order:
#   1. Asks the user to enter a number “x” 
#   2. Asks the user to enter a number “y”
#   3. Prints out number “x”, raised to the power “y”. 
#   4. Prints out the log (base 2) of “x”.
import math

def getPower(x, y):
    return pow(x, y)
    
def getLogBase2(x):
    return math.log2(x)

x = float( input("Enter number x: ") )
y = float( input("Enter number y: ") )

print("x**y =", getPower(x, y))
print("log(x) =", getLogBase2(x))
