import sys
input = sys.stdin.readline

n = int(input())
nums = [-1]
for _ in range(n):
    nums.append(int(input()))

memos = [[0,0], [nums[1],nums[1]]]

