import sys


def dfs(cnt, idx):
    global answer

    if cnt == m:
        sum = 0
        for x1, y1 in houses:
            tmp = float('inf')
            for x2, y2 in candidates:
                tmp = min(tmp, abs(x1 - x2) + abs(y1 - y2))
            sum += tmp
        answer = min(answer, sum)
    else:
        for i in range(idx, len(pizzas)):
            candidates[cnt] = pizzas[i]
            dfs(cnt + 1, i + 1)


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = []
    houses = []
    pizzas = []

    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        for j in range(n):
            if row[j] == 1:
                houses.append((i, j))
            elif row[j] == 2:
                pizzas.append((i, j))

    candidates = [0] * m
    answer = float('inf')
    dfs(0, 0)
    print(answer)
