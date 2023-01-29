n = int(input())
s = []
for i in range(n):
	first, second = map(int, input().split())
	s.append([first, second])
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])
last = 0
cnt = 0
for start, end in s:
	if start >= last:
		cnt += 1
		last = end
print(cnt)

# 회의가 겹치지 않으면서 최대 수를 구해야한다.
# 입력 받은 숫자들을 정렬을 해야하는데
# 회의의 시작시간과 끝나는 시간이 같을 수 있으므로
# 시작시간을 기준으로 정렬을 먼저 해준뒤
# 끝나는 시간을 기준으로 정렬을 한번 더 해준다. 
# for문을 돌려 시작 시간이 끝나는 시간보다 크거나 같을경우
# cnt를 1 증가시켜 준다.

import sys
input = sys.stdin.readline

N = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(N)]

def sort_key(x):
    return (x[1], x[0])

schedules.sort(key=lambda x: (x[1], x[0]))

count = 0
prev_end = 0
for start, end in schedules:
    if start >= prev_end:
        prev_end = end
        count += 1

print(count)