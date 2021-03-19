'''
A
B C
D E F
G H I J
.
.
n lines
'''
n=eval(input('Enter the no.of lines : '))
ch=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end=' ')
        ch+=1
    print()
