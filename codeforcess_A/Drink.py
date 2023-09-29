def res(drinks,per):
    result=0
    for i in per:
        result+=(per/100)
    return " {0:.12f}".format((res/drinks)*100)

if __name__=="__main__":
 drink=float(input())
 pere=tuple(map(float,input().split()))
 
 print (res(drink,pere)   ) 