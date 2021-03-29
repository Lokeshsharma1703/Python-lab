'''
Program to find the number of currency notes of each type (Rs. 2000, Rs. 500 and Rs. 100),
when the total number of currency notes counted altogether is minimum and there must be at
least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user
'''
a=int(input('Enter the ammount : '))
a-=100
print('Notes of 2000 : ',a//2000)
print('Notes of 500 : ',(a%2000)//500)
print('Notes of 100 : ',(a%500)//100 + 1)