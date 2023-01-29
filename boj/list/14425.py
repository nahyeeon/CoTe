import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0

for _ in range(m):
    arr = set(input())
    if len(arr) == n:
        cnt += 1
        
print(cnt)
## 오답


## 정답
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = set([input() for _ in range(N)])
cnt = 0
for _ in range(M):
    t = input()
    if t in s:
        cnt += 1
print(cnt)