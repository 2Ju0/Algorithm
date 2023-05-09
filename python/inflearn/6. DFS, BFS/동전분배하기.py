import sys


def dfs(cnt):
    global answer

    if cnt == n:
        differ = max(arr) - min(arr)
        if differ < answer:
            tmp = set()
            for v in arr:
                tmp.add(v)
            if len(tmp) == 3:
                answer = differ
    else:
        for i in range(3):
            arr[i] += coins[cnt]
            dfs(cnt + 1)
            arr[i] -= coins[cnt]


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    coins = [int(input()) for _ in range(n)]
    arr = [0, 0, 0]
    answer = float('inf')

    dfs(0)
    print(answer)
