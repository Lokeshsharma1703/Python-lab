'''
    H
   HHH
  HHHHH
 HHHHHHH
HHHHHHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
  HHHHH            HHHHH
                 HHHHHHHHH
                  HHHHHHH
                   HHHHH
                    HHH
                     H
'''

n=int(input('Enter a number : '))
for i in range(1,n+1):
    print((' '*(n-i)),'H'*(2*i-1))
for i in range(1,n+2):
    width=2*n-1
    w=3*n-1
    print(('H'*n).center(width,' '),('H'*n).rjust(w,' '))
for i in range(1,n//2+1):
    print(' ','H'*(5*n))
for i in range(1,n+2):
    width=2*n-1
    w=3*n-1
    print(('H'*n).center(width,' '),('H'*n).rjust(w,' '))
for i in range(n,0,-1):
    print((' '*(3*n)),' '*(n-i),'H'*(2*i-1))