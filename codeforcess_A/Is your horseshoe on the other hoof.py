s1, s2, s3, s4 = map(int, input().split())

# Calculate the number of different colors
num_colors = len(set([s1, s2, s3, s4]))

# Calculate the minimum number of horseshoes to buy
min_horseshoes = 4 - num_colors

print(min_horseshoes)