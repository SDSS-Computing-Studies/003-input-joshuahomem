#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704

side1=input("enter in length of side 1")
side2=input("enter in length of side 2")
side2=float(side2)
side1=float(side1)
side3=side1**2+side2**2
import math
side3=float(side3)
print ("math.sqrt(side3) : ", math.sqrt(side3))
