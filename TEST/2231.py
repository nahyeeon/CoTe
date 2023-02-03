n = int(input())

def generate(n):
    answer = n
    str_n = str(n)
    for i in str_n:
        answer += int(i)
    return answer

result = 0
for i in range(1,n+1):
    if generate(i)==n:
        result = i
        break

print(result)