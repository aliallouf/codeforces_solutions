n=int(input())
d=list(input().split())
d=[int(i) for i in d]
a,b= tuple(map(int, input().split())) 
result=0  
for i in range(a-1,b-1):
    result+=d[i]
print(result)    