n = int(input())
cnt = 0

for x in range(1,n+1):
    if x <= 99:
        cnt += 1
    elif x == 1000:
        pass
    else:
        str_x = str(x)
        if int(str_x[0]) - int(str_x[1]) == int(str_x[1]) - int(str_x[2]):
            cnt += 1
            

print(cnt)