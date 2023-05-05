import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    words = set(input().strip() for _ in range(n))
    poem = set(input().strip() for _ in range(n - 1))

    print(''.join(words - poem))
