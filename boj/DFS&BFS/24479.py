import sys
input = sys.stdin.readline

e, v, start = map(int, input().split())

graph = []
for _ in range(v+1):
    graph.append([])
    
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (v+1)

from collections import deque

def dfs(start, graph, visited):
    stack = deque()
    
    stack.append(start)
    
    while stack:
        now_v = stack.pop()
        if visited[now_v]:
            continue
        visited = 
        print(now_v)