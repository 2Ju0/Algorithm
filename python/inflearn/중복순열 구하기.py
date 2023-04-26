import sys


def dfs(cnt):
    global total

    if cnt == m:
        print(' '.join([str(num) for num in result]))
        total += 1
        return
    else:
        for i in range(1, n + 1):
            result[cnt] = i
            dfs(cnt + 1)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    result = [0] * m
    total = 0

    dfs(0)
    print(total)
