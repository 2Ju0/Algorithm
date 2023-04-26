import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())

    result = n // k
    
    # while True:
    #     if n == 1:
    #         break
    #     n -= 1
    #     if n % k == 0:
    #         n //= k
    #     result += 1

    print(result)
