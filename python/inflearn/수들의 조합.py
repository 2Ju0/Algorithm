import sys


def dfs(cnt, idx):
    global total

    if cnt == k:
        if sum(result) % m == 0:
            total += 1
        return
    if idx == n:
        return
    else:
        result[cnt] = nums[idx]
        dfs(cnt + 1, idx + 1)
        dfs(cnt, idx + 1)


if __name__ == "__main__":
    input = sys.stdin.readline

    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = int(input())

    result = [0] * k
    total = 0

    dfs(0, 0)
    print(total)
