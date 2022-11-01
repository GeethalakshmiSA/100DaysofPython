# PROBLEM STATEMENT - Find the area of circle
# Formula - Area of Circle = pi * (r**2)

# Method - 1 : Using In-built functions

import math
rad = float(input("Enter the radius of the circle : "))
area = math.pi * pow(rad,2)
print("Area of the circle is %.6f" % area)

# Method - 2 : Simple calculation

def area(r):
    pi = 3.142
    return pi * (r**2)
    
rad = float(input("Enter the radius of the circle : "))
print("Area of the circle is ", area(rad))
