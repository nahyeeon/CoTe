fixed, variable, selling = map(int, input().split())

if variable > selling:
    print(-1)
else:
    i = 1
    while fixed+variable*i >= selling*i:
        i += 1
    print(i)
    
    