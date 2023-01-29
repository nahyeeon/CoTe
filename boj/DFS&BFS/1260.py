import sys
from collections import deque

def dfs(start, graph, visited):
    stack = deque()
    
    stack.append(start)
    
    while stack:
        now_v = stack.pop()
        if visited[now_v]:
            continue
        visited[now_v] = True
        print(now_v, end=" ")
        for next_v in graph[now_v][::-1]:
            stack.append(next_v)

def bfs(start, graph, bfs_visited):
    queue = deque()
    
    bfs_visited[start] = True
    queue.append(start)
    
    while queue:
        now_v = queue.popleft()
        print(now_v, end = " ")
        for next_v in graph[now_v]:
            if bfs_visited[next_v]:
                continue
            bfs_visited[next_v] = True
            queue.append(next_v)
    

input = sys.stdin.readline

v, e, start = map(int, input().split())

graph = []
for _ in range(v+1):
    graph.append([])
    
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for link in graph:
    link.sort()

visited = [False] * (v+1)
bfs_visited = [False] * (v+1)


dfs(start, graph, visited)
print()
bfs(start, graph, bfs_visited)