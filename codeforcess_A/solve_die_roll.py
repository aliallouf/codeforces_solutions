
import math
Y,W=tuple(map(int, input().split()))

Max=max(Y,W)

p=6-Max+1
d=6
if p%2==0 and d%2==0:
    p=p//2
    d=d//2
   
if p%3==0 and d%3==0:
   p=p//3
   d=d//3
print(p,d,sep="/") 
    