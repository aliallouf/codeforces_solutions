
s = input()#1st
t = input()#2se

row = ord(t[0]) - ord(s[0])
vertical = int(t[1]) - int(s[1])

a= max(abs(vertical), abs(row))
print(a)

while row or vertical:
    a = ""
    if row > 0:
        row -= 1
        a += "R"
    if row < 0:
        row += 1
        a += "L"
    if vertical > 0:
        vertical -= 1
        a += "U"
    if vertical < 0:
        vertical += 1
        a += "D"
    print(a)