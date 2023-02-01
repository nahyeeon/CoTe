import sys
input = sys.stdin.readline

n = int(input())
nums = [-1]
for _ in range(n):
    nums.append(int(input()))

memos = [[0,0], [nums[1],nums[1]]]


for i in range(2, n+1):
    memos.append([memos[i-1][1] + nums[i], max(memos[i-2]) + nums[i]])

print(max(memos[n]))