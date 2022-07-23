import sys
from collections import deque #Stack, Queue의 기능 모두 가진 객체
input=sys.stdin.readline

N,M,V=map(int,input().split())
visited=[False]*(N+1)

graph=[[] for _ in range(N+1)]


for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for _, attr in enumerate(graph):
    attr.sort()

def dfs(V):
    print(V,end=' ')
    visited[V]=True
    for i in graph[V]:
        if not visited[i]:
            dfs(i)
            visited[i]=True

def bfs(V):
    queue=deque([V])
    visited[V]=True
    while queue:
        V=queue.popleft()
        print(V,end=' ')
        for i in graph[V]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
dfs(V)
print()
visited=[False]*(N+1)
bfs(V)