import sys
from collections import deque


def bfs(x, y):
    global cnt

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '1':
                graph[nx][ny] = '0'
                queue.append((nx, ny))
                cnt += 1


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    answer = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1':
                graph[i][j] = '0'
                cnt = 1
                bfs(i, j)
                answer.append(cnt)

    answer.sort()
    print(len(answer))
    for v in answer:
        print(v)
