if __name__ == '__main__':
    n = int(input())
    b=tuple(map(int, input().split()))
    min = 0
    b = tuple(sorted(b))
    for i in range(n-1):
        if b[i] != b[i+1]:
            min =b[i+1]
            break
if min !=0:
    print(min)
else:
    print('NO')            
        
        
       
        