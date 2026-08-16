import math
x = 9.
print (math.pi)
print (math.e)
result = math.sqrt(x) #square root
result = math.ceil(x)
result = math.floor(x)

import math
# Area of the circle
radius = float(input("Enter the radius of the circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area, 2)}cm^2")

import math
#finding hypotenuse of the right triangle
a = int(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The answer is: {c}")