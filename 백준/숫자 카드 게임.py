import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    result = 0
    for _ in range(n):
        cards = list(map(int, sys.stdin.readline().split()))
        min_value = min(cards)
        result = max(result, min_value)

    print(result)
