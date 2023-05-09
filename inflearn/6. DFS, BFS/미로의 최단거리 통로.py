import sys
from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline

    graph = [list(map(int, input().split())) for _ in range(7)]
    dis = [[0] * 7 for _ in range(7)]

    que = deque()
    que.append((0, 0))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while que:
        x, y = que.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < 7 and 0 <= next_y < 7 and graph[next_x][next_y] == 0:
                graph[next_x][next_y] = 1
                dis[next_x][next_y] = dis[x][y] + 1
                que.append((next_x, next_y))

    if dis[6][6] == 0:
        print(-1)
    else:
        print(dis[6][6])
