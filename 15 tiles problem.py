# Program that calculates the number of rectangular tiles required to cover a rectangular floor if
# the dimensions of the floor and the dimensions of a tile are entered by the user.
rl=eval(input('Enter the length of room : '))
rb=eval(input('Enter the breadth of room : '))
tl=eval(input('Enter the length of tile : '))
tb=eval(input('Enter the breadth of tile : '))
l=rl/tl
b=rb/tb
a=l*b
print('Total no. of tiles required : %.1f'%a)