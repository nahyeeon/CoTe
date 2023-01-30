import sys
input = sys.stdin.readline

word = input().rstrip()

answers = [-1] * 26

for i in range(len(word)):
    idx = ord(word[i]) - 97
    if answers[idx] == -1:
        answers[idx] = i
        
for answer in answers:
    print(answer , end=" ")