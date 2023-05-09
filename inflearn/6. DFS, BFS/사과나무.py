import sys
from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    visited[n // 2][n // 2] = 1

    que = deque()
    que.append((n // 2, n // 2))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    answer = graph[n // 2][n // 2]
    print(answer)
    cnt = 0
    while cnt < n // 2:
        for _ in range(len(que)):
            x, y = que.popleft()

            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]

                if 0 <= next_x < n and 0 <= next_y < n:
                    if not visited[next_x][next_y]:
                        visited[next_x][next_y] = 1
                        answer += graph[next_x][next_y]
                        que.append((next_x, next_y))

        cnt += 1

    print(answer)
