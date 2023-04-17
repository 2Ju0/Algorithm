import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    dx = [-1, 0, 1, 0]  # 상 우 하 좌
    dy = [0, 1, 0, -1]

    dQ = deque()
    dQ.append((n // 2, n // 2))

    level = 0
    result = graph[n // 2][n // 2]
    visited[n // 2][n // 2] = 1

    while dQ:
        if level == n // 2:
            break

        for _ in range(len(dQ)):
            x, y = dQ.popleft()

            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]

                if 0 <= next_x < n and 0 <= next_y < n:
                    if not visited[next_x][next_y]:
                        visited[next_x][next_y] = 1
                        result += graph[next_x][next_y]
                        dQ.append((next_x, next_y))
                        print(x, y, next_x, next_y, dQ, graph[next_x][next_y], result)

        level += 1

print(result)
