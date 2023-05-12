import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    w, n = map(int, input().split())
    jewels = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    jewels.sort(key=lambda x: -x[1])

    for weight, value in jewels:
        if w >= weight:
            answer += (weight * value)
            w -= weight
        else:
            answer += (w * value)
            break

    print(answer)
