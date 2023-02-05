
def printLock(lock):
    for i in range(len(lock)):
        print(lock[i])


def turn_key(key):
    return list(zip(*key[::-1]))


def check(key_crash_displacements, lock_unlock_locations):
    # unlock
    # print("lock_unlock_locations", key_crash_displacements)
    for current_x, current_y in lock_unlock_locations:
        can_unlock = []
        for trial in key_crash_displacements:
            if m-1 <= current_x+trial[0] < n+m-1 and m-1 <= current_y+trial[1] < n+m-1:
                can_unlock.append((current_x+trial[0], current_y+trial[1]))
        # currents displacement isn't same with unlock locations of lock(0)
        can_unlock.sort()
        # print(can_unlock, lock_unlock_locations)
        if can_unlock != lock_unlock_locations:
            # print("different")
            continue
        else:
            return True
            # # displacement to location(std of key (0,0))
            # current_x -= std_1location[0]
            # current_y -= std_1location[1]
            # # print(current_x, current_y)
            # # print("key_unlock_locations", key_unlock_locations)
            # for trial in key_unlock_locations:
            #     if m-1 <= current_x+trial[0] < n+m-1 and m-1 <= current_y+trial[1] < n+m-1:
            #         if expanded_lock[current_x+trial[0]][current_y+trial[1]] == 0:
            #             # print("current", current_x +
            #             #       trial[0], current_y+trial[1])
            #             # print("can't open!")
            #             break
            #     return True


def findChar(lock, char):
    locations = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == char:
                locations.append((i, j))
    return locations


def makeDisplacement(locations):
    std_x, std_y = locations[0][0], locations[0][1]
    displacements = []
    for i in range(len(locations)):
        displacements.append((locations[i][0]-std_x, locations[i][1]-std_y))
    return displacements


def expand_lock(lock):  # m: size of key
    k = n+2*(m-1)
    expanded_lock = [[0]*(k) for _ in range(k)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            expanded_lock[i+(m-1)][j+(m-1)] = lock[i][j]
    return expanded_lock


def solution(key, lock):
    global n, m
    n, m = len(lock), len(key)

    expanded_lock = expand_lock(lock)

    # for current_x in range(m-1, n+m-1):
    #     for current_y in range(m-1, n+m-1):
    #         print(current_x, current_y)
    for _ in range(4):

        key = turn_key(key)
        # key_unlock_locations = findChar(key, 0)
        # key_unlock_displacements = makeDisplacement(key_unlock_locations)

        # std_1location = (findChar(key, 1)[0][0], findChar(key, 1)[0][1])
        key_crash_displacements = makeDisplacement(findChar(key, 1))

        # displacement needs a starting point(initializes to (0,0))
        lock_unlock_locations = [(x, y) for x, y in findChar(
            expanded_lock, 0) if m-1 <= x < n+m-1 and m-1 <= y < n+m-1]
        # lock_crash_locations = [(x, y) for x, y in findChar(
        #     expanded_lock, 1) if m-1 <= x < n+m-1 and m-1 <= y < n+m-1]
        # print(lock_unlock_locations)

        if check(key_crash_displacements,  lock_unlock_locations):
            return True
    return False


key = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]  # False
# # key = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]  # True
lock = [[1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [
    1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]

# key = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]
# lock = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]

print(solution(key, lock))
