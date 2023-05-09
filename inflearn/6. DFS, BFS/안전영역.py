import sys
from collections import deque


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

        for i in range(n):
            for j in range(n):
                if graph[i][j] > v and not visited[i][j]:
                    que.append((i, j))
                    visited[i][j] = 1

                    while que:
                        x, y = que.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > v and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                que.append((nx, ny))

                    cnt += 1

        if answer < cnt:
            answer = cnt

    print(answer)
