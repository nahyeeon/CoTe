def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0]-1
        end = i[1]
        arr = array[start:end]
        arr.sort()
        tmp = i[2]-1
        answer.append(arr[tmp])
    return answer