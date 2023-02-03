import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

cnt = 0
for coin in coins[::-1]:
    if k >= coin:
        cnt += k // coin
        k = k % coin
        
print(cnt)