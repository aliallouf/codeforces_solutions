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
    n = int(input())
shapes = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20,
}
total_faces = 0

for _ in range(n):
    shape = input()
    total_faces += shapes[shape]

print(total_faces)
    """
