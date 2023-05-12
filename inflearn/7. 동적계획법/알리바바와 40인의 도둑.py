import sys
from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = graph[0][0]

    que = deque()
    que.append((0, 0))

    while que:
        x, y = que.popleft()

        for dx, dy in [(1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                tmp = dp[x][y] + graph[nx][ny]
                if dp[nx][ny] == 0 or (dp[nx][ny] != 0 and tmp < dp[nx][ny]):
                    dp[nx][ny] = tmp
                    que.append((nx, ny))

    print(dp[n - 1][n - 1])
