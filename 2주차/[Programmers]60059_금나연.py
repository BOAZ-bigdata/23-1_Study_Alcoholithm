
# def printLock(lock):
#     for i in range(len(lock)):
#         print(lock[i])


def turn_key(key):
    return list(zip(*key[::-1]))


def check(attached_lock):
    for x in range(m-1, n+m-1):
        for y in range(m-1, n+m-1):
            if attached_lock[x][y] != 1:
                return False
    return True


def expand_lock(lock, m):  # m: size of key
    k = n+2*(m-1)
    expanded_lock = [[0]*(k) for _ in range(k)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            expanded_lock[i+(m-1)][j+(m-1)] = lock[i][j]
    return expanded_lock


def attach(i, j, lock, key):
    for x in range(m):
        for y in range(m):
            lock[i+x][j+y] += key[x][y]


def detach(i, j, lock, key):
    for x in range(m):
        for y in range(m):
            lock[i+x][j+y] -= key[x][y]


def solution(key, lock):
    global n, m
    n, m = len(lock), len(key)

    expanded_lock = expand_lock(lock, m)
    for _ in range(4):
        for i in range(n+m-1):
            for j in range(n+m-1):
                attach(i, j, expanded_lock, key)
                if check(expanded_lock):
                    return True
                detach(i, j, expanded_lock, key)
        key = turn_key(key)
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]  # False
# key = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]  # True
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
