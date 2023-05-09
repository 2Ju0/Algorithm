import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    word1 = input().strip()
    word2 = input().strip()

    map1 = dict()
    map2 = dict()

    for v in word1:
        map1[v] = map1.get(v, 0) + 1
    for v in word2:
        map2[v] = map2.get(v, 0) + 1

    for (k, v) in map1.items():
        if map2.get(k) != v:
            print("NO")
            break
    else:
        print("YES")
