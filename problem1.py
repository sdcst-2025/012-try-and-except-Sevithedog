#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')
import math

print("Enter in the coefficients for a quadratic equation in the format:")
print("ax^2 + bx + c = 0")
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
except: 
    print("Invalid Values")
    exit()
try: 
    root1 = round((-b + math.sqrt(b**2 - 4*a*c))/(2*a),2)
    root2 = round((-b - math.sqrt(b**2 - 4*a*c))/(2*a),2)
    print(f"The roots of the equation are: {root1}, {root2}")
except:
    try:
        root = round((-b + math.sqrt(b**2 - 4*a*c))/(2*a),2)
        print(f"The root of the equation is {root}")
    except:
        try:
            root = round((-b - math.sqrt(b**2 - 4*a*c))/(2*a),2)
            print(f"The root of the equation is {root}")
        except:
            print("The equation has no real roots")

