def name(s):
    result=list(set(s))
    even="CHAT WITH HER!"
    odd="IGNORE HIM!"
    if len(result) % 2==0:
        return even
    else :
        return odd
    
S=list(input())
print(name(S))