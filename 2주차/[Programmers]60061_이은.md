# [Programmers 60061.기둥과 보 설치](https://school.programmers.co.kr/learn/courses/30/lessons/60061)
## 👾 풀이
  ### **`구현`**
- 문제를 처음 봤을 때는 어려워 보였지만, 잘 읽고 규칙대로 구현할 수만 있다면 나름 쉬웠던(?) 문제였.
- 우선 3차원 배열 check를 생성한다.
  - 초기에 check[x][y] = [False, False] 값을 갖는다.
  - check[x][y][a]는 x좌표, y좌표, a는 구조물 종류(0은 기둥, 1은 보)를 나타낸다.
  - 구조물이 존재하면 check[x][y][a] = True, 존재하지 않으면 False로 나타냈다.
- 문제에서 제시한 규칙대로 기둥 설치, 보 설치 함수를 먼저 작성하였다.
- 기둥 삭제, 보 삭제 함수는 다음과 같이 작성했다.
  - 먼저 해당 아이템(기둥 또는 보)을 삭제한다. -> `check[x][y][a] = False`
  - 해당 아이템을 삭제했을 때 영향을 받게되는 인접한 아이템들을 체크한다. -> 그림 그려서 생각했음..
  - 인접한 아이템이 존재하고, 아이템을 설치할 수 없을 때는 원상복귀한다. -> `check[x][y][a] = True`
- check 배열을 순회하면서 True인 값들을 찾아서 x, y 좌표와 구조물 종류를 배열에 담아서 result 배열에 append 해준다.
- x, y 좌표 순서대로 순회하고, 기둥이 0번째 인덱스, 보를 1번째 인덱스로 구분했기 때문에 문제에서 요구한 정렬 조건에 맞게 result 배열에 값이 순서대로 들어간다. (따라서 따로 정렬을 해줄 필요가 없다.)
- 중간에 테스트 케이스 2/3가 틀려서 좌절했는데, 인덱스 실수였다.. `check[x][y+1][1]` 인데, `check[x+1][y+1][1]` 로 적어놔서 그랬던 것... ㅠ 이런 실수는 사전에 어떻게 방지해야 할깝쑝 ; -;
## 👾 코드
~~~python
def solution(n, build_frame):
    check = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]
    
    # 기둥 설치
    def install_gi(x, y):
        # 바닥 위
        if y == 0:
            return True
        # 보의 한쪽 끝 위
        if check[x-1][y][1] or check[x][y][1]:
            return True
        # 다른 기둥 위
        if check[x][y-1][0]:
            return True

        return False

    # 보 설치
    def install_bo(x, y):
        # 한쪽 끝이 기둥 위
        if check[x][y-1][0] or check[x+1][y-1][0]:
            return True
        # 양쪽 끝이 다른 보
        elif check[x-1][y][1] and check[x+1][y][1]:
            return True

        return False

    # 기둥 삭제
    def remove_gi(x, y):
        check[x][y][0] = False # 기둥 삭제
        # 위쪽 기둥 체크
        if check[x][y+1][0] and not install_gi(x, y+1):
            return False
        # 기둥 위쪽의 양 옆 보 체크
        if check[x-1][y+1][1] and not install_bo(x-1, y+1):
            return False
        if check[x][y+1][1] and not install_bo(x, y+1):
            return False

        return True

    # 보 삭제
    def remove_bo(x, y):
        check[x][y][1] = False # 보 삭제
        # 양 옆 보 체크
        if check[x-1][y][1] and not install_bo(x-1, y):
            return False
        if check[x+1][y][1] and not install_bo(x+1, y):
            return False
        # 왼쪽, 오른쪽 위에 있는 기둥 체크
        if check[x][y][0] and not install_gi(x, y):
            return False
        if check[x+1][y][0] and not install_gi(x+1, y):
            return False

        return True

    
    for x, y, a, b in build_frame:
        if a == 0: # 기둥
            if b == 0 and not remove_gi(x, y): # 삭제
                check[x][y][0] = True # 원상복귀
            elif b == 1 and install_gi(x, y): # 설치
                check[x][y][0] = True
        elif a == 1: # 보
            if b == 0 and not remove_bo(x, y): # 삭제
                check[x][y][1] = True # 원상복귀
            elif b == 1 and install_bo(x, y): # 설치
                check[x][y][1] = True
    
    result = []
    for i in range(n+1):
        for j in range(n+1):
            if check[i][j][0]:
                result.append([i, j, 0])
            if check[i][j][1]:
                result.append([i, j, 1])

    return result
~~~