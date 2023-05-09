import sys


def dfs(x, y):
    global cnt

    cnt += 1
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny)


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    answer = []

    for _ in range(n):
        line = input().strip()
        arr = []
        for v in line:
            arr.append(int(v))
        graph.append(arr)

    for x in range(n):
        for y in range(n):
            if graph[x][y] == 1:
                cnt = 0
                dfs(x, y)
                answer.append(cnt)

    answer.sort()
    print(len(answer))
    for v in answer:
        print(v)
