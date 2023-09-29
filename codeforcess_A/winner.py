n=int (input())
c=0
dict={}
a,b=list(map(str,(input().split())))
b=int(b)
dict[a]=b
max=b
while c<n-1 :
    a,b=list(map(str,(input().split())))
    b=int(b)
    if a in dict:
        dict[a]=dict.get(a)+b
    else:
        dict[a]=b
    if dict.get(a)>max  :
        max=int(dict.get(a))
        ind =a
 
    c=c+1
print (ind)