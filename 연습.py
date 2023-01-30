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