# [Programmers 92344: 파괴되지 않은 건물](https://school.programmers.co.kr/learn/courses/30/lessons/92344)

Brute-force 알고리즘을 적용하면 `250,000 * 1,000 * 1,000`의 시간 복잡도를 가지기 때문에 효율성 테스트를 통과할 수 없다.

따라서 `skill`의 행 길이가 최대 250,000이므로 해당 부분을 해결하는 것이 문제의 포인트다. (`board`의 각 원소를 필연적으로 수정 및 조회해야하기 때문)

아마도 시간 복잡도를 `250,000 + 1,000 * 1,000`으로 감쇠시킬 수 있는 알고리즘을 개발해야할 것이다.

최종적으로 구간 합을 이용해 풀 수 있었다.

---

# 최종 코드

~~~python
def solution(board, skill):
    answer = 0
    convert = {1: -1, 2: 1}
    N, M = len(board), len(board[0])
    cum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for typ, r1, c1, r2, c2, degree in skill:
        cum[r1][c1] += convert[typ] * degree
        cum[r1][c2 + 1] -= convert[typ] * degree
        cum[r2 + 1][c1] -= convert[typ] * degree
        cum[r2 + 1][c2 + 1] += convert[typ] * degree
    for i in range(N + 1):
        for j in range(1, M + 1):
            cum[i][j] += cum[i][j - 1]
    for i in range(1, N + 1):
        for j in range(M + 1):
            cum[i][j] += cum[i - 1][j]
    for i in range(N):
        for j in range(M):
            if 0 < board[i][j] + cum[i][j]:
                answer += 1
    return answer
~~~

---

# Legacy 코드

~~~python
def solution(board, skill):
    answer = 0
    convert = {1: -1, 2: 1}
    for s in skill:
        for i in range(s[1], s[3] + 1):
            for j in range(s[2], s[4] + 1):
                board[i][j] += convert[s[0]] * s[5]
    for i in board:
        for j in i:
            if j > 0:
                answer += 1
    return answer
~~~

> 채점 결과

+ 정확성: 53.8 (100%)
+ 효율성: 0.0 (0%)
+ 합계: 53.8 / 100.0

~~~python
def solution(board, skill):
    answer = 0
    convert = {1: -1, 2: 1}
    tar = []
    for s in skill:
        for i in range(s[1], s[3] + 1):
            for j in range(s[2], s[4] + 1):
                board[i][j] += convert[s[0]] * s[5]
                if board[i][j] <= 0 and not (i, j) in tar:
                    tar.append((i, j))
                elif board[i][j] > 0 and (i, j) in tar:
                    tar.remove((i, j))
    answer = len(board) * len(board[0]) - len(tar)
    return answer
~~~

> 채점 결과

+ 정확성: 53.8 (100%)
+ 효율성: 0.0 (0%)
+ 합계: 53.8 / 100.0