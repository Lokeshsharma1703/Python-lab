# Program to find the Simple Interest and the total amount when the Principal, Rate of Interest
# and Time are entered by the user.
p,r,t=map(float,input('Enter the principle, rate, time respectively : ').split())
print('Simple interest = ',(p*r*t)/100)