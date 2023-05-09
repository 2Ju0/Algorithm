import sys


def dfs(x, y):
    global answer

    if x == 6 and y == 6:
        answer += 1
    else:
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < 7 and 0 <= next_y < 7 and graph[next_x][next_y] == 0:
                graph[next_x][next_y] = 1
                dfs(next_x, next_y)
                graph[next_x][next_y] = 0


if __name__ == "__main__":
    input = sys.stdin.readline
    graph = [list(map(int, input().split())) for _ in range(7)]
    graph[0][0] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    answer = 0
    dfs(0, 0)
    print(answer)
