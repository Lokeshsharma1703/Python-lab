'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
no. of lines = 5
'''
n=int(input('Enter a number : '))
for i in range(1,n+1):
    ch=97+n-1
    for j in range(1,n-i+1):
        print('-',end='-')
    for k in range(1,i+1):
        print(chr(ch),end='-')
        ch-=1
    ch+=2
    for k in range(1, i):
        if k != n - 1:
            print(chr(ch), end='-')
            ch += 1
        else:
            print(chr(ch), end='')
            ch += 1
    for i in range(1,2*(n-i+1)-2):
        print('-',end='')
    print()
for i in range(1,n):
    ch=97+n-1
    for i in range(1,i+1):
        print('-',end='-')
    for k in range(1,n-i+1):
        print(chr(ch),end='-')
        ch-=1
    ch+=2
    for k in range(1,n-i):
        print(chr(ch),end='-')
        ch+=1
    for i in range(1,2*(i+1)-2):
        print('-',end='')
    print()