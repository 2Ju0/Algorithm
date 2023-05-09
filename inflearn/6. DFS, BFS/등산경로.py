import sys
from collections import deque


def dfs(x, y):
    global answer

    if x == ex and y == ey:
        answer += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[x][y] < graph[nx][ny]:
                    visited[nx][ny] = 1
                    dfs(nx, ny)
                    visited[nx][ny] = 0


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = []
    min = float('inf')
    max = -float('inf')
    sx, sy = 0, 0
    ex, ey = 0, 0

    for i in range(n):
        arr = list(map(int, input().split()))
        graph.append(arr)
        for j in range(n):
            if arr[j] < min:
                min = arr[j]
                sx, sy = i, j
            elif arr[j] > max:
                max = arr[j]
                ex, ey = i, j

    que = deque()
    que.append((sx, sy))

    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    answer = 0
    dfs(sx, sy)
    print(answer)
