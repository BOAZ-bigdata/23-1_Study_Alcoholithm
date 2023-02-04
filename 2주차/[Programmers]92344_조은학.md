# 92344 파괴되지 않은 건물


- 순수한 풀이
```python
def solution(board, skill):
    # 건물 0이하 파괴
    # 회복 스킬로 내구도 상승

    normal = 0
    # 파괴되지 않은 건물 수 return
    for i in range(len(skill)):
        if(skill[i][0]==1):
            for p in range(skill[i][1], skill[i][3]+1):
                for q in range(skill[i][2], skill[i][4]+1):
                    board[p][q] = board[p][q] - skill[i][5]
        elif(skill[i][0]==2):
            for p in range(skill[i][1], skill[i][3]+1):
                for q in range(skill[i][2], skill[i][4]+1):
                    board[p][q] = board[p][q] + skill[i][5]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] > 0):
                normal = normal + 1

    return normal
```


### 전 너무 순수해서 더이상 풀 수 없을 것 같습니다.