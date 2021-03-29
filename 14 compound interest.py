#  Program to find the Compound Interest compounded annually and the total amount when the
# Principal, Rate of Interest and Time are entered by the user.
p,r,t= map(float,input('Enter the principle, rate, time respectively : ').split())
print('Compound interest = ',p*((1+r/100)**t)-p)