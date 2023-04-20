import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    for i in range(n):
        word = input().strip().lower()
        reversed_word = word[::-1]

        if word == reversed_word:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))
