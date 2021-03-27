'''
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''
n=int(input('Enter a number : '))
p=n
for i in range(1,n+1):
    m=n
    for j in range(1,i+1):
        print(m,end=' ')
        m-=1
    for j in range(1,n-i+1):
        print(p,end=' ')
    for j in range(1,n-i+1):
        print(p,end=' ')
    p -= 1
    m=n-i+2
    for j in range(1,i):
        print(m,end=' ')
        m+=1
    print()
for i in range(1,n):
    q=n
    for j in range(1,n-i):
        print(q,end=' ')
        q-=1
    r=n-i
    r=(n-r)+1
    for j in range(1,i+2):
        print(r,end=' ')
    for j in range(1,i+1):
        print(i+1,end=' ')
    s = i+2
    for j in range(1, n - i):
        print(s, end=' ')
        s += 1
    print()