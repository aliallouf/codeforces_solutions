if __name__ == "__main__":
    list = 0 
    n = int(input())
    colors = input()
    for i in range(len(colors)-1):
        if colors[i] == colors[i+1]:
            list+=1
    print(list)    