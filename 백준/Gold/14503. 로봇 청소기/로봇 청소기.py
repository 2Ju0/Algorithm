import sys


def turn():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while True:
        if room[x][y] == 0:
            room[x][y] = 2
            answer += 1
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if room[nx][ny] == 0:
                turn()
                front_x, front_y = x + dx[d], y + dy[d]
                if room[front_x][front_y] == 0:
                    x, y = front_x, front_y
                break
        else:
            back_x, back_y = x - dx[d], y - dy[d]
            if room[back_x][back_y] == 1:
                break
            x, y = back_x, back_y

    print(answer)
