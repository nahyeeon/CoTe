from collections import Counter

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
num_counter = Counter(num)
most_num = num_counter.most_common(1)


print(most_num[0][0])