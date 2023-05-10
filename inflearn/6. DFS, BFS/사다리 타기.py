import sys


def dfs(x, y):
    if x == 0:
        print(y)
        sys.exit(0)
    else:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 10 and 0 <= ny < 10 and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)


if __name__ == "__main__":
    input = sys.stdin.readline

    graph = [list(map(int, input().split())) for _ in range(10)]
    x, y = (9, graph[9].index(2))
    graph[x][y] = 0

    dx = [0, 0, -1]  # 우, 좌, 상
    dy = [1, -1, 0]

    dfs(x, y)
