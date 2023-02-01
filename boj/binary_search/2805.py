# N, M = map(int, input().split())
# tree = list(map(int, input().split()))
# start, end = 1, max(tree) #이분탐색 검색 범위 설정

# while start <= end: #적절한 벌목 높이를 찾는 알고리즘
#     mid = (start+end) // 2
    
#     log = 0 #벌목된 나무 총합
#     for i in tree:
#         if i >= mid:
#             log += i - mid
    
#     #벌목 높이를 이분탐색
#     if log >= M:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)







import sys
input = sys.stdin.readline

def binary_search(trees, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        y_mid = 0
        for tree in trees:
            if tree > mid:
                y_mid += tree - mid
        if y_mid < target:
            right = mid -1
        else:
            left = mid +1
    return right

n, target = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 1, max(trees)

print(binary_search(trees,target, left, right))