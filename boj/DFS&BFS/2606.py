import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, visited):
    # 0 push pop print 0 push
    queue = deque()
    visited[start] = True
    queue.append(start)
    
    while queue:
        now_v = queue.popleft()
        for next_v in graph[now_v]:
            if visited[next_v]:
                continue
            visited[next_v] = True
            
            queue.append(next_v)
    

v = int(input())
n = int(input())
start = 1

graph = []
for _ in range(v+1):
    graph.append([])
    
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (v+1)

bfs(start, graph, visited)

print(sum(visited)-1)