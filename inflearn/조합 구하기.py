import sys


def dfs(v, cnt):
    global total

    if cnt == m:
        total += 1
        print(' '.join([str(num) for num in result]))
        return
    if v > n:
        return
    else:
        result[cnt] = v
        dfs(v + 1, cnt + 1)
        dfs(v + 1, cnt)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    result = [0] * m
    total = 0

    dfs(1, 0)
    print(total)

