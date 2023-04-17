import sys

def dfs(v):
    if v > 7:
        return
    else:
        print(v)
        dfs(2*v)
        dfs(2*v+1)


if __name__ == "__main__":
    # n = int(sys.stdin.readline())
    dfs(1)
