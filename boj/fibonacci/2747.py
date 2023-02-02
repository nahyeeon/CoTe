import sys
input = sys.stdin.readline
n = int(input())

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(n))
# 시간초과(오답)

# 정답
memo = [0] * 50
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n]:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]
    
    
n = int(input())
print(fibo(n))