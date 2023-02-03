import sys
from collections import deque
input = sys.stdin.readline

v, e = map(int,input().split())
start = 1
graph = []
for _ in range(v+1):
    graph.append([])
    
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
    
# 정답
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,start):
    # 0 push pop print 0 push
    num = [0] * (n+1)
    queue = deque()
    visited[start] = True
    queue.append(start)
    while queue:
        now_v = queue.popleft()
        for next_v in graph[now_v]:
            if visited[next_v]:
                continue
            visited[next_v] = True
            num[next_v] = num[now_v]+1
            queue.append(next_v)
    return sum(num)

result = [-1]
for i in range(1,n+1):
    visited = [False] * (n+1)
    result.append(bfs(graph,i))
print(result.index(min(result[1:])))


#내코드로 만들기
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
result = [-1]
for i in range(1, n+1):
    visited = [False] * (v+1)
    result.append(bfs(graph,i))
    
