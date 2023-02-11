import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num, arr = input().split()
    text = ''
    for i in arr:
        text += i*int(num)
    print(text)