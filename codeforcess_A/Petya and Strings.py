s1 = input()
s2 = input()
if s1.lower() < s2.lower():
    print(-1)
if s2.lower() < s1.lower():
    print(1)
if s1.lower() == s2.lower():
    print(0)        