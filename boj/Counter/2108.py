from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
nums_counter = Counter(nums)
most_nums = nums_counter.most_common()
idx = n//2
if len(nums)<2:
    idx = 0
else:
    idx = idx

print(round(sum(nums)/n))
print(nums[idx])
if len(nums)<2:
    print(most_nums[0][0])
elif most_nums[0][1] == most_nums[1][1]:
    print(most_nums[1][0])
else:
    print(most_nums[0][0])

print(max(nums)-min(nums))