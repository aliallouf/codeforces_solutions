n,m=tuple(map(int, input().split()))
r=0
pre=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
for i in range(0,15):
    if(n==pre[i] and m==pre[i+1]):
        r+=1
        break
if  r==0 :
       print("NO") 
else:
       print("YES")    