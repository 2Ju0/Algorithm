import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    arr = [str(i) for i in range(1, 21)]

    for _ in range(10):
        begin, end = map(int, input().split())
        arr = arr[:begin-1] + arr[end-21:begin-22:-1] + arr[end:]

    print(" ".join(arr))
