import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]

nums.sort(key = lambda x : (x[1], x[0]))


cnt = 0
last = 0
for start, end in nums:
    if last <= start:
        cnt += 1
        last = end
    else:
        continue
        
print(cnt)