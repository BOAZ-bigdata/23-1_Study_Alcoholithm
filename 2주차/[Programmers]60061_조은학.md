- 한 줄 요약
1. 삼성 스타일 빡구현 프로그래밍 문제
```python

# 유효한지 확인
def isValid(answer):
    for x,y,a in answer:
        #기둥인 경우, 바닥 위, 보의 한쪽 끝 부분, 다른 기둥 위를 검사
        if a == 0:
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            return False
        #보인 경우, 한쪽 끝 부분이 기둥 위, 또는 양 쪽 끝 부분이 보와 연결을 검사
        elif a == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,a,b = frame
        # 삭제
        if b==0:
            answer.remove([x,y,a])
            if not isValid(answer):
                answer.append([x,y,a])

        # 설치
        elif b==1:
            answer.append([x,y,a])
            if not isValid(answer):
                answer.remove([x,y,a])
    return sorted(answer)
```