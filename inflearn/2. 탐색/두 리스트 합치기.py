import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    n = input()
    first = list(map(int, input().split()))
    m = input()
    second = list(map(int, input().split()))

    arr = [str(num) for num in sorted(first + second)]
    print(" ".join(arr))
