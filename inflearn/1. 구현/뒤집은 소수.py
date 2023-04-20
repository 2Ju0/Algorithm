import sys
import math


def reverse(x):
    reversed_x = x[::-1]
    reversed_x = int(reversed_x.lstrip("0"))

    return reversed_x


def isPrime(x):
    res = True

    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            res = False

    return res


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    nums = list(input().split())

    for num in nums:
        reversed_num = reverse(num)
        if isPrime(reversed_num):
            print(reversed_num, end=" ")
