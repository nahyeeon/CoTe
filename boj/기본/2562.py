import sys
input = sys.stdin.readline
nums = [int(input()) for _ in range(9)]

maxx = max(nums)
print(maxx)

max_index = nums.index(maxx) +1
print(max_index)