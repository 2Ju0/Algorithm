import sys


def dfs(idx, sum):
    if sum > total // 2:
        return
    if idx == n:
        if total // 2 == sum:
            print("YES")
            sys.exit(0)
    else:
        dfs(idx + 1, sum + arr[idx])
        dfs(idx + 1, sum)


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    total = sum(arr)
    dfs(0, 0)
    print("NO")
