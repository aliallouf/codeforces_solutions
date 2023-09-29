s=input()
a=0
if s[0]=='h':
    a+=1
b=True
for i in range(1,len(s)):
    if s[i]==s[i-1] and b:
        continue
    if s[i]=="hello"[a]:
        if a==4:
            a+=1
            break
        a+=1
        if a==3:b=False
        else:b=True
        continue
if a==5:
    print("YES")
else:
    print("NO")                