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
        key = turn_key(copy.deepcopy(key))
    return False
```
