# [Programmers 60059: 자물쇠와 열쇠](https://school.programmers.co.kr/learn/courses/30/lessons/60059)

진짜 내 자식 같이 개발한 문제입니다...

해당 문제는 머리로 이해하긴 매우 쉽지만 구현하는 것이 어려웠습니다...

새로운 `key`를 만들어서 이동하고 회전하면 시간 복잡도가 너무 커질 것 같아서 `key`의 좌표를 회전된 것처럼 맵핑해줄 수 있는 `convert_func` 함수를 개발하였습니다. ~~는 행렬 다시 만들고 이동 및 회전해도 풀 수 있음;~~

`key`와 `lock`이 겹쳐지는 순간 겹쳐지지 않은 `key`의 부분을 쉽게 고려하기 위해 `for`문을 `M` (`len(key)`)에 대해 개발하였고, 해당 부분을 위해 `key`를 회전하는 것은 `lock`을 회전하는 것과 같은 성질을 이용해 `lock`을 회전하였습니다.

또한 `lock`의 모든 부분에 일일히 `key`를 넣어보며 확인하면 시간 복잡도가 커질 것 같아서 `key`의 삽입이 필요한 구간을 `idx_i_1`, `idx_j_1`, `idx_i_2`, `idx_j_2`로 정의하였습니다. ~~는 이것도 그냥 풀 수 있음;~~

최종적으로 꼭 `key`의 삽입이 필요한 구간에 대해서만 완벽히 일치하는지에 대한 여부 확인을 위한 함수 `match`를 수행하였습니다.

---

# 최종 코드

~~~python
import sys

def convert_func(rot, s1, s2, idx_i_1, idx_j_1, idx_i_2, idx_j_2, i, j):
    if rot == 0:
        ni, nj = i + idx_i_1 - s1, j + idx_j_1 - s2
    elif rot == 1:
        ni, nj = -j + idx_i_2 + s1, i + idx_j_1 - s2
    elif rot == 2:
        ni, nj = -i + idx_i_2 + s1, -j + idx_j_2 + s2
    elif rot == 3:
        ni, nj = j + idx_i_1 - s1, -i + idx_j_2 + s2
    return ni, nj

def match(rot, key, M, lock, N, s1, s2, idx_i, idx_j, idx_i_1, idx_j_1, idx_i_2, idx_j_2):
    for i in range(M):
        for j in range(M):
            ni, nj = convert_func(rot, s1, s2, idx_i_1, idx_j_1, idx_i_2, idx_j_2, i, j)
            if (0 <= ni < N) and (0 <= nj < N):
                if (idx_i_1 <= ni <= idx_i_2) and (idx_j_1 <= nj <= idx_j_2):
                    if key[i][j] == lock[ni][nj]:
                        return False
                    else:
                        continue
                else:
                    if key[i][j] == 1:
                        return False
                    else:
                        continue
            else:
                continue
    return True

def solution(key, lock):
    keyRange = [[], []]
    N, M = len(lock), len(key)
    idx_i_1, idx_j_1, idx_i_2, idx_j_2 = sys.maxsize, sys.maxsize, 0, 0
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                idx_i_1 = min(idx_i_1, i)
                idx_j_1 = min(idx_j_1, j)
                idx_i_2 = max(idx_i_2, i)
                idx_j_2 = max(idx_j_2, j)
    if idx_i_1 == sys.maxsize:
        return True
    idx_i, idx_j = idx_i_2 - idx_i_1, idx_j_2 - idx_j_1
    if idx_i + 1 > M or idx_j + 1 > M:
        return False
    for rot in range(4):
        for s1 in range(M - idx_i):
            for s2 in range(M - idx_j):
                if match(rot, key, M, lock, N, s1, s2, idx_i, idx_j, idx_i_1, idx_j_1, idx_i_2, idx_j_2):
                    return True
    return False
~~~