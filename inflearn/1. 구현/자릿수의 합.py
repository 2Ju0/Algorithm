import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    nums = list(input().split())

    max_sum = 0
    res = 0

    for num in nums:
        tmp = sum([int(i) for i in num])

        if max_sum < tmp:
            max_sum = tmp
            res = num

    print(res)
