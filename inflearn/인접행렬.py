import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    result = [[0] * n for _ in range(n)]

    for _ in range(m):
        start, end, price = map(int, input().split())
        result[start-1][end-1] = price

    for lst in result:
        print(' '.join([str(num) for num in lst]))
