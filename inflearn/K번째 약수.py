import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    result = [1]
    for i in range(2, n+1):
        if n % i == 0:
            result.append(i)

    if len(result) < k:
        print(-1)
    else:
        print(result[k-1])