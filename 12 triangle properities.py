# Program to find whether a triangle is scalene, isosceles, right angled or invalid when the sides of
# the triangle are entered by the user.
a,b,c=map(float,input('Enter the sides of triangle : ').split())
if a+b>c or a+c>b or b+c>a:
    if c**2==a**2 + b**2 or b**2==a**2 + c**2 or a**2==b**2 + c**2:
        print('Triangle is right angled')
    elif a==b and a!=c or a==c and a!=b or b==c and b!=a:
        print('Triangle is isoscale')
    elif a!=b!=c:
        print('Triangle is scelene')
else:
    print('Invalid sides')