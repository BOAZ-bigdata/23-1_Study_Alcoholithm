# [Programmers 60059: 자물쇠와 열쇠](https://school.programmers.co.kr/learn/courses/30/lessons/60059)

`#simulation` `#sliding_window`

---

## 접근
### 뭘 고정하고 뭘 움직일까
- 문제 잘 읽기: key맵과 lock맵은 사이즈가 다를 수 있음
- key를 움직이든 lock을 움직이든 똑같을 듯
- 하지만 key맵 사이즈가 lock맵 사이즈보다 항상 같거나 작다고 하니
- lock맵 고정하고 key맵을 움직여봐야징
### 기본적인 이동함수 구현 필요
- 행렬을 90도씩 회전시켜주는 함수
### key가 lock맵에 맞는지 어떻게 체크할까?
- 음... sliding window 방식으로 하나하나 대조해봐야 할 듯
### key가 lock맵을 초과하는 경우는 어떻게 처리할까?
- lock맵을 초과하는 key의 일부 좌표를 무시할 수는 없다 -> 일부 좌표를 버림으로써 원래 불가능한데 가능해지는 경우가 발생할 수 있음
- sliding window 쓰는 김에 pooling 처리까지 해줘서 하면
- 완벽한 convolution...

## 풀이
- `def:turn` 시계방향 90도 회전 함수 구현
- `lock_map` 기존의 lock맵을 상하좌우로 len(key맵) 만큼 pooling 시켜줌
- **sliding window** 방식으로 전체 `lock_map`을 순회하며 matched=True인지 체크
    - `lock_map`이 아닌 기존의 lock맵 내부에 한하여 lock맵과 key맵이 매치되는지 체크
    - 매치될 때, lock맵의 값이 0(홈)이라면 매치된 홈 개수를 카운트 해주어
    - 최종적으로 lock맵과 key맵(일부가 될 수도 있음)이 매치 되었는지 (matched=True),  
    남아도는 lock맵의 홈이 없는지(hom == cnt) 체크

---

## 전체 코드

```python	
def turn(m): # 시계방향 90도 회전
    N = len(m)
    new_m = [[0]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            new_m[b][N-1-a] = m[a][b]
    return new_m


def solution(key, lock):
    # lock padding len(key)된 새로운 lock맵 정의, lock hom 개수 저장
    lock_map = [[0]*(len(key)*2+len(lock)) for _ in range(len(key)*2+len(lock))]

    hom = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 1:
                lock_map[i+len(key)][j+len(key)] = 1 # 돌기 표시
            else:
                hom += 1


    # lock 고정, key맵을 이동 및 회전하며 체크
    for _ in range(4): # 360 돌리면서 체크
        # sliding window
        for h in range(len(lock_map)-len(key)+1): # 아래로 순회하면서 체크
            for w in range(len(lock_map)-len(key)+1): # 오른쪽으로 순회하면서 체크
                # key맵 사이즈 window 째로 체크 
                cnt = 0
                matched = True
                for oh in range(len(key)):
                    for ow in range(len(key)): 
                        if len(key) <= w+ow < len(lock) + len(key) and len(key) <= h+oh < len(lock) + len(key):
                            if lock_map[h+oh][w+ow] + key[oh][ow] != 1:
                                matched = False
                                break
                            elif lock_map[h+oh][w+ow] == 0:
                                cnt += 1
                    if not matched:
                        break
                if matched and hom == cnt:
                    return True  
        key = turn(key)

    return False


```

### 헤맸던 거
- 한 칸씩 움직이는 move 함수는 굳이 구현해줄 필요가 없다
- key맵을 직접 `lock_map` 위에 올려보지 않아도
- `lock_map`에 key맵 사이즈 만큼의 범위를 체크하면서
- `lock_map`이 아닌 원래 lock맵에 대한 인덱스값(ow, oh)만 가지고
- key맵에 대입해서 확인해보면 된다