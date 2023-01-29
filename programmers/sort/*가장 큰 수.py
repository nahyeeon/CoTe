def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(str(i))
        
    answer.sort(key=lambda x : x*3,reverse=True)
    return str(int(''.join(answer)))