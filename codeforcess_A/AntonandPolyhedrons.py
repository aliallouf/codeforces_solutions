n = int(input())
s = []
for i in range(n):
    a = input()
    s.append(a)
c = 0
for i in s:
    if i == 'Tetrahedron':
        c += 4
    if i == 'Cube':
        c += 6    
    if i == 'Octahedron':
        c += 8
    if i == 'Dodecahedron':
        c += 12
    if i == 'Icosahedron':
        c += 20
        
print(c)                    

    """
    
    """