import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    t = int(input())

    for i in range(t):
        n, s, e, k = map(int, input().split())
        nums = list(map(int, input().split()))
        arr = sorted(nums[s-1:e])
        print("#%d %d" % (i+1, arr[k-1]))
