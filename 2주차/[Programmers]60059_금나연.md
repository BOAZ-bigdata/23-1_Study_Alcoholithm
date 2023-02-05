# [Programmers 60059] 자물쇠와 열쇠

## 문제 요약

1. `N\*N` 자물쇠와 `M*M` 열쇠

- key와 lock의 원소는 `0` 또는 `1`로 이루어져 있음
  - `0`은 홈 부분, `1`은 돌기 부분

2. 자물쇠의 홈 부분에 열쇠의 돌기 부분이 정확하게 들어맞도록 열쇠를 회전하고 평행이동

## 목표

가능한지(True), 불가능한지(False)

### 예제 입력

```
key=[
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
    ]

lock=[
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
    ]
```

### 예제 출력

```
True
```

## 풀이

- `Simulation`

### 1트

- 상대적인 위상을 저장해서 bfs로 나머지를 맞춰볼까 했음
  => 생각보다 복잡해서 시간 안에 못할 것 같아 넘어가기로 함
  => 해봤는데 잘 안 됨,, 맨 뒤 참고

### 2트

- 빡구현
  - 이중배열 회전시키는 거 찾아봄.. 레전드..
- 미친 for loop.. 너무 더러워서 함수화를 좀 많이 함

### 주요 논리

#### 1. 자물쇠 확장

```
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 0, 0]
[0, 0, 1, 1, 0, 0, 0]
[0, 0, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
```

- 한 면에 n+2(m-1)개로 확장

```python
def expand_lock(lock, m):
    k = n+2*(m-1)
    expanded_lock = [[0]*(k) for _ in range(k)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            expanded_lock[i+(m-1)][j+(m-1)] = lock[i][j]
    return expanded_lock
```

#### 2. 자물쇠와 열쇠를 attach/detach

```python
def attach(i, j, lock, key):
    for x in range(m):
        for y in range(m):
            lock[i+x][j+y] += key[x][y]


def detach(i, j, lock, key):
    for x in range(m):
        for y in range(m):
            lock[i+x][j+y] -= key[x][y]
```

- lock과 key의 해당 부분 합으로 구현

#### 3. 자물쇠와 열쇠가 들어맞는지 check

```python
def check(attached_lock):
    for x in range(m-1, n+m-1):
        for y in range(m-1, n+m-1):
            if attached_lock[x][y] != 1:
                return False
    return True
```

- 합이 1일 경우 잘 맞음
  - 0일 경우 부족함
  - 2일 경우 충돌

## 전체 코드

```python
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
```

## 1트 논리

### 1. key의 1 위치와 lock의 0 위치를 파악한다

```python
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
```

- findChar()는 절대적인 location을 반환하고, makeDisplacement()는 상대적인 위치(변위)를 반환한다.
  ex)

```
0 1 0
1 0 0
1 0 0
```

- `findChar(key, 1)` = [(0, 1), (1, 0), (2, 0)]
- `makeDisplacement(findChar(key,1))` = [(0, 0), (-1, 1), (-2, 1)]

### 2. 알맞는지 체크

```python
def check(expanded_lock, key_unlock_displacements, key_crash_displacements, lock_unlock_locations, lock_crash_locations, std_1location, key_unlock_locations):
    # unlock
    for current_x, current_y in lock_unlock_locations:
        can_unlock = []
        for trial in key_crash_displacements:
            if m-1 <= current_x+trial[0] < n+m-1 and m-1 <= current_y+trial[1] < n+m-1:
                can_unlock.append((current_x+trial[0], current_y+trial[1]))
        # currents displacement isn't same with unlock locations of lock(0)
        can_unlock.sort()
        if can_unlock != lock_unlock_locations:
            continue
        else:
            return True

```

```
for x, y in (lock의 0 위치):
    for 변위 in (key의 1 변위 list):
        x, y에 변위를 더해서 실제 lock에 해당하는 index range에 있을 때 can_unlock list에 append
    if (can_unlock list가 lock의 0 위치와 정확하게 일치):
        return True
    else: continue
```

### 전체 코드(54.0/100.0)

```python
def turn_key(key):
    return list(zip(*key[::-1]))

def check(key_crash_displacements, lock_unlock_locations):
    # unlock
    for current_x, current_y in lock_unlock_locations:
        can_unlock = []
        for trial in key_crash_displacements:
            if m-1 <= current_x+trial[0] < n+m-1 and m-1 <= current_y+trial[1] < n+m-1:
                can_unlock.append((current_x+trial[0], current_y+trial[1]))
        # currents displacement isn't same with unlock locations of lock(0)
        can_unlock.sort()
        if can_unlock != lock_unlock_locations:
            continue
        else:
            return True


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

    for _ in range(4):

        key = turn_key(key)
        key_crash_displacements = makeDisplacement(findChar(key, 1))
        # displacement needs a starting point(initializes to (0,0))
        lock_unlock_locations = [(x, y) for x, y in findChar(
            expanded_lock, 0) if m-1 <= x < n+m-1 and m-1 <= y < n+m-1]

        if check(key_crash_displacements,  lock_unlock_locations):
            return True
    return False
```
