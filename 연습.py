import sys
from collections import deque

def dfs(start, graph, dfs_visited):
    stack = deque()

    stack.append(start)
    
    while stack:
        now_v = stack.pop()
        if dfs_visited[now_v]:
            continue
        dfs_visited[now_v] = True
        print(now_v, end=" ")
        for next_v in graph[now_v][::-1]:
            stack.append(next_v)
            
def bfs(start, graph, bfs_visited):
    queue = deque()
    
    bfs_visited[start] = True
    queue.append(start)
    
    while queue:
        now_v = queue.popleft()
        print(now_v, end=" ")
        for next_v in graph[now_v]:
            if bfs_visited[next_v]:
                continue
            bfs_visited[next_v] = True
            queue.append(next_v)

v, e, start = map(int, input().split())

input = sys.stdin.readline

graph = []
for _ in range(v+1):
    graph.append([])
    
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for link in graph:
    link.sort()
    
dfs_visited = [False] * (v+1)
bfs_visited = [False] * (v+1)

dfs(start, graph, dfs_visited)
print()
bfs(start, graph, bfs_visited)





import sys
from collections import deque

def bfs(start, graph, bfs_visited):
    # push 전 visit(0 push pop print 0 push)
    queue = deque()
    bfs_visited[start] = True
    queue.append(start)
    
    while queue:
        now_v = queue.popleft()
        print(now_v, end= " ")
        for next_v in graph[now_v]:
            if bfs_visited[next_v]:
                continue
            bfs_visited[next_v] = True
            queue.append(next_v)
    
        
def dfs(start, graph, dfs_visoted):
    # print 전 visit(push pop 0 print push)
    stack = deque()
    stack.append(start)
    
    while stack:
        now_v = stack.pop()
        if dfs_visited[now_v]:
            continue
        dfs_visited[now_v]=True
        print(now_v, end = " ")
        for next_v in graph[now_v][::-1]:
            stack.append(next_v)

intput = sys.stdin.readline

v, e, start = map(int, input().split())

graph = []

for _ in range(v+1):
    graph.append([])
    
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for line in graph:
    line.sort()
    
bfs_visited = [False] * (v+1)
dfs_visited = [False] * (v+1)

bfs(start, graph, bfs_visited)
print()
dfs(start, graph, dfs_visited)

import sys
input = sys.stdin.readline

def binary_search(lans, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        y_mid = 0
        for lan in lans:
            y_mid += lan // mid
        if y_mid < target:
            right = mid - 1
        elif y_mid >= target:
            left = mid + 1
    return right

k, target = map(int, input().split())

lans =[int(input()) for _ in range(k)]

left, right = 1, max(lans)
print(binary_search(lans, target, left, right))


def binary_search(lans, target, left, right):
    while left <= right:
        mid = (left+ right)// 2
        y_mid = 0
        for lan in lans:
            y_mid += lan // mid
        if y_mid >= target:
            left = mid +1
        elif y_mid < target:
            right = mid -1
    return right
        

import sys
input = sys.stdin.readline

def binary_search(nums, targets, left, right):
    while left <= right:
        mid = (left + right) // 2
        y_mid = nums[mid]
        if y_mid < targets:
            left = mid +1
        elif y_mid > targets:
            right = mid -1
        elif y_mid == target:
            return mid
    return -1
            

n = int(input())
nums = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

nums.sort()
left, right = 0, len(nums)-1

for target in targets:
    if binary_search(nums, target, left, right) == -1:
        print(0)
    else:
        print(1)
        
        
import sys
input = sys.stdin.readline

def binary_search(trees, target, left, right):
    while left <= right:
        mid = (left+right) // 2
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

print(binary_search(trees, target, left, right))

import sys
input = sys.stdin.readline

N = int(input().rstrip())

def is_hansoo(x):
    if x < 100:
        return True
    if x == 1000:
        return False
    str_x = str(x)
    if int(str_x[0]) - int(str_x[1]) == int(str_x[1])-int(str_x[2]):
        return True
    return False

cnt = 0
for i in range(1, N+1):
    if is_hansoo(i):
        cnt += 1
print(cnt)


import sys
input = sys.stdin.readline

n = int(input())

def is_hansoo(x):
    if x < 100:
        return True
    if x == 1000:
        return False
    str_x = str(x)
    if int(str_x[0]) - int(str_x[1]) == int(str_x[1]) - int(str_x[2]):
        return True
    return False

cnt = 0
for i in range(1, n+1):
    if is_hansoo(i):
        cnt += 1
        
print(cnt)

import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    temp = i + sum(map(int, str(i)))
    
    if temp == n:
        result = i
        break
    
print(result)


