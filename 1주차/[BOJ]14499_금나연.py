# def printMap(map):
#     for i in range(len(map)):
#         print(map[i])
N, M, X, Y, K = map(int, input().split())
dmap = []
direction = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]  # E, W, N, S

for i in range(N):
    dmap.append(list(map(int, input().split())))

moves = list(map(int, input().split()))


def roll(dir, dice):  # Top, N, E, S, W, Bottom
    d1, d2, d3, d4, d5, d6 = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1:  # E
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d5, d2, d1, d4, d6, d3
        return dice
    elif dir == 2:  # W
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d3, d2, d6, d4, d1, d5
        return dice
    elif dir == 3:  # N
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d4, d1, d3, d6, d5, d2
        return dice
    elif dir == 4:  # S
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d2, d6, d3, d1, d5, d4
        return dice


def move():
    cx, cy = X, Y
    dice = [0, 0, 0, 0, 0, 0]  # Top, N, E, S, W, Bottom
    for m in moves:
        nx = cx+direction[m][0]
        ny = cy+direction[m][1]
        if -1 < nx < N and -1 < ny < M:  # vaild move
            dice = roll(m, dice)
            if dmap[nx][ny] == 0:
                dmap[nx][ny] = dice[5]
            else:
                dice[5] = dmap[nx][ny]
                dmap[nx][ny] = 0
            print(dice[0])
            cx, cy = nx, ny
        else:
            continue


move()
