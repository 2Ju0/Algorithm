import sys

if __name__ == "__main__":
    W, N = map(int, sys.stdin.readline().rstrip().split())

    jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    jewels.sort(key=lambda x: -x[1])
    result = 0

    for weight, price in jewels:
        if W >= weight:
            result += (price * weight)
            W -= weight
        else:
            result += (W * price)
            break

    print(result)
