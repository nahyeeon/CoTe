def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(str(i))
        
    answer.sort(key=lambda x : x*3,reverse=True)  # 1+1+1=3 1x3=3 "1"x3="111" "a"+"a"+"a"="aaa"
    return str(int(''.join(answer)))




