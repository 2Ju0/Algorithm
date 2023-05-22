import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph=[[0]*(n+1) for _ in range(n+1)]
    degree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        degree[b] += 1

    que = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            que.append(i)

    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if graph[v][i] == 1:
                degree[i] -= 1
                if degree[i] == 0:
                    que.append(i)
