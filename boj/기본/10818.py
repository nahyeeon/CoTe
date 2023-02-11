import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
answer = []
answer.append(min(nums))
answer.append(max(nums))

print(answer[0], answer[1])