import sys
from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline

    m, n = map(int, input().split())
    graph = []
    dis = [[0] * m for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    que = deque()

    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        for j in range(m):
            if row[j] == 1:
                que.append((i, j))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                que.append((nx, ny))
                dis[nx][ny] = dis[x][y] + 1

    is_all_ripen = True
    for row in graph:
        if any(v == 0 for v in row):
            is_all_ripen = False

    answer = 0
    if is_all_ripen:
        for row in dis:
            for v in row:
                answer = max(answer, v)
        print(answer)
    else:
        print(-1)
