n = int(input())
memos = [0, 1]

for i in range(2, n+1):
    fibo = memos[i-1] + memos[i-2]
    memos.append(fibo)
    
print(memos[n])