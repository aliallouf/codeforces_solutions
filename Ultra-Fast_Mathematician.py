# a=input()
# b=input()
# for i in range(len(a)):
#     if a[i]==b[i]:
#         print('0',end="")
#     else:
#         print('1',end="")    
#####################################
s1 , s2 = input() , input()

for i in range(len(s1)):
    print(0 if s1[i] == s2[i] else 1, end="")