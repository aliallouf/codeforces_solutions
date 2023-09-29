n=int(input())
name=['o']*n
fibo=[1,1]

for i in range(2,n+1):
    fibo+=fibo[i-1]+fibo[i-2],    
a=1
b=1
while(a!=n+1):
    if a>fibo[b]:
        b+=1
    if a==fibo[b]:
        
        name[a-1]='O'
        b+=1
    a+=1
    
print(''.join(name))        