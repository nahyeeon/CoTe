import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
maxx = max(nums)
result = 0
for i in range(n):
    result += nums[i]/maxx*100
    
print(result/n)