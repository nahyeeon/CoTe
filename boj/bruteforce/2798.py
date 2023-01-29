import sys
input  = sys.stdin.readline

start, end = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(start):
    for j in range(i+1, start):
        for k in range(j+1, start):
            if arr[i] + arr[j] + arr[k] > end:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])
                
print(result)
