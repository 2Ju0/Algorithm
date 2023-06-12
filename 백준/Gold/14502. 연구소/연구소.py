import sys


def dfs(x, y):
    global infected

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if infected[nx][ny] == 1: continue
        if graph[nx][ny] == 1: continue
        infected[nx][ny] = 1
        dfs(nx, ny)


def spread():
    global infected

    for x, y in virus:
        infected[x][y] = 1
        dfs(x, y)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and infected[i][j] == 0:
                cnt += 1

    return cnt


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    infected = [[0] * m for _ in range(n)]
    graph = []
    blank = []
    virus = []
    answer = 0

    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

        for j in range(len(row)):
            if row[j] == 0:
                blank.append((i, j))
            if row[j] == 2:
                virus.append((i, j))

    l = len(blank)
    for i in range(l):
        for j in range(i + 1, l):
            for k in range(j + 1, l):
                graph[blank[i][0]][blank[i][1]] = 1
                graph[blank[j][0]][blank[j][1]] = 1
                graph[blank[k][0]][blank[k][1]] = 1

                answer = max(answer, spread())

                infected = [[0] * m for _ in range(n)]
                graph[blank[i][0]][blank[i][1]] = 0
                graph[blank[j][0]][blank[j][1]] = 0
                graph[blank[k][0]][blank[k][1]] = 0

    print(answer)
