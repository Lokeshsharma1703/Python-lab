n=int(input('Enter a number : '))
m=n
sum=0
while n>0:
    sum=sum+(n%10)**3
    n=n//10
if sum==m:
    print('Armstrong number')
else:
    print('Not armstrong number')
