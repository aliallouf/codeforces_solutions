
s= input()
i=0
s1=''
while(i<len(s)):
    if s[i]=='.':
        s1+='0'
        i+=1
    elif s[i]=='-' and s[i+1]=='-':
        s1+='2'
        i+=2
    else:
        s1+='1'
        i+=2
print(s1)        
"""s=input()
s1=''
lens=len(s)
for i in range(0,lens):
    if s[i]=='.':
        s1+='0'
    if s[i]=='-' and s[i+1]=='.':
        s1+='1'
        i=i+1
    if s[i]=='-' and s[i+1]=='-':
        s1+='2'
        i=i+1
print(s1)              """