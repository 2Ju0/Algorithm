import sys
from collections import deque

sys.setrecursionlimit(10 ** 5)


def dfs(x, y, v):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > v:
            dfs(nx, ny, v)


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = []
    largest = -float('inf')
    smallest = float('inf')
    answer = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    que = deque()

    for _ in range(n):
        line = list(map(int, input().split()))
        graph.append(line)
        if largest < max(line):
            largest = max(line)
        elif smallest > min(line):
            smallest = min(line)

    for v in range(smallest, largest):
        cnt = 0
        visited = [[0] * n for _ in range(n)]

        for x in range(n):
            for y in range(n):
                if graph[x][y] > v and not visited[x][y]:
                    cnt += 1
                    dfs(x, y, v)

        answer = max(answer, cnt)

    print(answer)

