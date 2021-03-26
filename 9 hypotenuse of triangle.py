#Program to find the hypotenuse of a right angled triangle, when the base and height are entered by the user.
import math
h=eval(input('Enter the height of triangle : '))
b=eval(input('Enter the base of triangle : '))
h=h**2 + b**2
print('Hypotenuse of triangle is : ',math.sqrt(h))

