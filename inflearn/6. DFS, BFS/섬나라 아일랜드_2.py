import sys
from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    que = deque()

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                que.append((i, j))
                graph[i][j] = 0
                
                while que:
                    x, y = que.popleft()
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                            graph[nx][ny] = 0
                            que.append((nx, ny))

                answer += 1

    print(answer)
