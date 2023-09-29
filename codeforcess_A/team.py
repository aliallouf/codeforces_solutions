n = int(input())
z = 0
for i in range(n ):
    a, b, c = tuple(map(int, input().split()))
    l1 = [a, b, c]
    if sum(l1) >= 2:
        z += 1
print(z)