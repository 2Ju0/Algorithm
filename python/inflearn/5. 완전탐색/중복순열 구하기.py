import sys


def dfs(cnt):
    global total

    if cnt == m:
        print(' '.join([str(i) for i in result]))
        total += 1
        return
    else:
        for i in range(1, n + 1):
            result[cnt] = i
            dfs(cnt + 1)


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    result = [0] * m
    total = 0

    dfs(0)
    print(total)
