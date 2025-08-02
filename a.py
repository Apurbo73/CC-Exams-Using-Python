import math
n = int(input())
for _ in range (n):
    a,b,c = map(int, input().split())
    d= a*b 
    e= d/2
    if e<c:
        print ("Yes")
    else:
        print("No")