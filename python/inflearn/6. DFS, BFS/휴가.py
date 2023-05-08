import sys


def dfs(t, p):
    global answer

    if t > n + 1:
        return
    if t == n + 1:
        if answer < p:
            answer = p
            return
    else:
        dfs(t + arr[t][0], p + arr[t][1])
        dfs(t + 1, p)


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = [[0, 0]]
    answer = 0
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    dfs(1, 0)
    print(answer)
