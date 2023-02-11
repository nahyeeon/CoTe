# n = int(input())

# answer = 0
# i=1
# while i <= n:
#     answer += i
#     i += 1
    
# print(answer)
    
    
# X= int(input())
# N= int(input())
# answer = 0

# i = 0
# while i < N:
#     a, b = map(int, input().split())
#     answer += a * b
#     i += 1
    
# if X==answer:
#     print("Yes")
# else:
#     print("No")
  
def is_pelindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False
          
    
while True:
    n = input()
    if n == '0':
        break
    if is_pelindrome(n):
        print('yes')
    else:
        print('no')
    
    
    
    # 반복문 돌리기(순서도/표)
    # 함수(순서도/표)-> 2753, 10818, 1259, 2609
    # 숙제  class 1, 2
    