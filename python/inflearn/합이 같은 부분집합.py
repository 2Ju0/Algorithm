import sys


def dfs(cnt, sum):
    if sum > total // 2:
        return

    if cnt == len(nums):
        if total - sum == sum:
            print("YES")
            sys.exit(0)
    else:
        dfs(cnt + 1, sum + nums[cnt])
        dfs(cnt + 1, sum)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    total = sum(nums)
    stack = []

    dfs(0, 0)
    print("NO")
