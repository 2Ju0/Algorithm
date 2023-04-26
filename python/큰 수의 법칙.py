import sys

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    numbers.sort(reverse=True)

    result = 0
    for _ in range(M):
        for _ in range(K):
            if M == 0:
                break
            result += numbers[0]
            M -= 1

        if M == 0:
            break
        result += numbers[1]
        M -= 1

    print(result)