# Program to input two numbers and print the swapped values of them.
a,b=map(eval,input('Enter the values of A and B respectively : ').split())
a,b=b,a
print(f'A = {a}\nB = {b}')
