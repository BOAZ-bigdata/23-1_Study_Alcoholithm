# 분할정복

## 분할정복이란?

- 주어진 문제를 두 개 이상의 부분 문제로 나누어 풀고 이를 병합하여 문제를 해결하는 알고리즘으로, Divide(분할) & Conquer(정복)이라고 한다.
- 예시: `이진탐색`, `퀵정렬`, `병합정렬`

## 분할 정복의 특징

- 분할된 문제들은 크기만 작아질 뿐 원래 문제와 성격이 동일하다(fractal).

- 대다수의 경우 재귀로 구현하나, 빠른 실행이나 부분 문제 해결 순서를 선택하기 위해, 스택(Stack), 큐(Queue)등의 자료구조를 이용하기도 한다.

- 문제를 매번 절반으로 나눌 수 없을 때까지 분할하는 시간 복잡도는 O(logN)이다.

## 알고리즘 설계

- Divide: 문제가 분할 가능할 경우 2개 이상의 문제로 나눈다.
- Conquer: 나누어진 문제가 여전히 분할 가능하면 다시 나누고, 그렇지 않으면 부분 문제를 푼다.
- Combine: 정복한 문제들을 병합하여 원래 문제의 답을 낸다.

# [샤워실 바닥 깔기(Small)](https://www.acmicpc.net/problem/14600)

## 문제 요약

1. 정사각형이고 한 변의 길이가 2의 제곱수인 샤워실에 3칸을 차지하는 ㄱ자 모양 타일을 사용하여 배수구의 위치 하나를 제외한 나머지 바닥을 덮어야 한다.

2. 입력

- 바닥의 한 변의 길이를 표현하는 자연수 K(1 ≤ K ≤ 2)
  - 바닥의 크기는 2^K
- 배수구의 위치를 나타내는 자연수 x, y (1 ≤ x, y ≤ 2K)
  - 가장 왼쪽 아래가 (1, 1), 가장 오른쪽 위가 (2K, 2K)

## 목표

ㄱ자 타일을 채우는 방법 찾기

- 각 타일마다 고유한 번호를 매긴 타일의 배치도를 출력
  - 각 타일의 번호에는 19000 이하의 자연수만을 사용
  - 배수구가 있는 위치는 -1로 표시
- 가능한 답 중 하나만 출력하면 된다.
- 만약 알맞게 타일을 배치하는 방법이 존재하지 않는다면 -1을 출력

### 예제 입력1

```
2
1 1
```

### 예제 출력1

```
4 4 5 5
4 3 3 5
1 1 3 2
-1 1 2 2
```

### 예제 입력2

```
2
3 2
```

### 예제 출력2

```
4 4 5 5
4 3 3 5
1 3 -1 2
1 1 2 2
```

### 주저리

- 모든 경우의 수에서 가능할까? yes!
- `L-트로미노 타일링`이라는 유명 문제로, 수학적 귀납법을 통해 배수구로 사용되는 한 칸을 제외하고 2의 제곱수를 한 변의 길이로 가지는 어떤 정사각 평면에서도 트로미노를 이용하여 평면을 채울 수 있다고 증명할 수 있다.

## 풀이

- `분할정복`

### 주요 논리

#### 1. 트로미노를 포함한 사분면에서 비어있는 평면을 향해 확인 후 재귀, 분할정복

- area로 사분할된 영역을 구분하여 각각 재귀로 계속한다.
- 0, 1, 2, 3은 시계방향으로 왼쪽 상단부터, 4는 중간 부분

#### 2.

## 전체 코드

```python
def solution(x, y, k, area):
    global num

    if k <= 1:
        cnt = 3  # tro-mino(3)
        if area == 0 or area == 4:
            for i in range(x, x+2):
                for j in range(y, y+2):
                    if not board[i][j] and cnt:
                        board[i][j] = num
                        cnt -= 1
        elif area == 1:
            for i in range(x, x+2):
                for j in range(y+1, y-1, -1):
                    if not board[i][j] and cnt:
                        board[i][j] = num
                        cnt -= 1
        elif area == 2:
            for i in range(x+1, x-1, -1):
                for j in range(y, y+2):
                    if not board[i][j] and cnt:
                        board[i][j] = num
                        cnt -= 1
        elif area == 3:
            for i in range(x+1, x-1, -1):
                for j in range(y+1, y-1, -1):
                    if not board[i][j] and cnt:
                        board[i][j] = num
                        cnt -= 1
        num += 1
        return
    solution(x, y, k-1, 0)
    solution(x, y+2**(k-1), k-1, 1)
    solution(x+2**(k-1), y, k-1, 2)
    solution(x+2**(k-1), y+2**(k-1), k-1, 3)
    solution(x+2**k//4, y+2**k//4, k-1, 4)


K = int(input())
X, Y = map(int, input().split(" "))
board = [[0]*2**K for _ in range(2**K)]
board[2**K - Y][X-1] = -1

num = 1

solution(0, 0, K, 0)

for row in board:
    for col in row:
        print(col, end=' ')
    print()

```

# 추가로 풀어볼만한 문제

- [샤워실 바닥 깔기(Large)](https://www.acmicpc.net/problem/14601)
