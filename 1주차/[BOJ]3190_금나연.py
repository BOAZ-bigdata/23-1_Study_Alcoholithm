# def printMap(map):
#     for i in range(len(map)):
#         print(map[i])
from collections import deque

N = int(input())
K = int(input())

# map
bmap = [[0]*(N+2) for _ in range(N+2)]
for i in range(N+2):
    if i == 0 or i == N+1:
        for j in range(N+2):
            bmap[i][j] = 1
            bmap[j][i] = 1
# apple
for i in range(K):
    x, y = map(int, input().split(" "))
    bmap[x][y] = 2

# turn
turn_list = []
L = int(input())
for _ in range(L):
    X, C = input().split(" ")
    turn_list.append((int(X), C))

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def turn(dir, C):
    if C == "L":
        dir = (dir+3) % 4
    else:
        dir = (dir+1) % 4
    return dir


def yummy():
    cur_time = 0
    dir = 1
    cx, cy = 1, 1
    bmap[cx][cy] = 1  # bamm
    tail = deque()
    tail.append((cx, cy))
    idx = 0  # turn index
    while True:
        nx = cx + direction[dir][0]
        ny = cy + direction[dir][1]
        # can proceed
        if bmap[nx][ny] != 1:
            if bmap[nx][ny] == 0:
                bmap[nx][ny] = 1
                tail.append((nx, ny))
                px, py = tail.popleft()
                bmap[px][py] = 0
            if bmap[nx][ny] == 2:
                bmap[nx][ny] == 1
                tail.append((nx, ny))
        else:
            cur_time += 1
            break
        cx, cy = nx, ny
        cur_time += 1

        if idx < L and cur_time == turn_list[idx][0]:
            # time X has come
            dir = turn(dir, turn_list[idx][1])
            idx += 1
    return print(cur_time)


# printMap(bmap)
yummy()
