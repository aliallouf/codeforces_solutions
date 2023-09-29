if __name__ == '__main__':
    l_a = list(map(int, input().split()))
    s = input()
    t_c = 0

    for c in s:
     t_c += l_a[int(c) - 1]
print(t_c)