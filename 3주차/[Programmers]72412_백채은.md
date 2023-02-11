# [Programmers 72412: 순위 검색](https://school.programmers.co.kr/learn/courses/30/lessons/72412)

## 문제
입력: `info[]` `query[]`
### `info[]`
점수 제외 각 영역에서 택1
- `언어` cpp / java / python
- `직군` backend / frontend
- `경력` junior / senior
- `소울푸드` chicken / pizza
- `점수`  1 ~ 100,000 (자연수)

### `query[]`
query의 각 문자열은 "[조건] X" 형식이며, [조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식의 문자열  
'-' 표시는 해당 조건을 고려하지 않겠다는 의미
- `언어` cpp / java / python / -
- `직군` backend / frontend / -
- `경력` junior / senior / -
- `소울푸드` chicken / pizza / -
- `X` 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미

<img width="841" alt="image" src="https://user-images.githubusercontent.com/88718806/218258183-11036451-2703-4fe8-bb3f-4379d5a84ff4.png">

## 풀이
- 조합
- 이분탐색

## code
~~~python
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    ### info
    info_dict = {}
    for i in range(len(info)):
        info_tmp = info[i].split(' ')
        info_dict_infos = info_tmp[:-1]
        info_dict_value = int(info_tmp[-1])
        
        for j in range(5):  # key들로 만들 수 있는 모든 조합(info_dict_key) 생성
            for c in combinations(info_dict_infos, j):
                info_dict_key = ''.join(c)
                if info_dict_key in info_dict:
                    info_dict[info_dict_key].append(info_dict_value)  # key들로 만든 조합(info_dict_key)에 value(->점수) 추가
                else:
                    info_dict[info_dict_key] = [info_dict_value]
                    
    for i in info_dict:
        info_dict[i].sort() # info_dict_key 당 value값들 정렬
                    
    ### query
    for i in range(len(query)):
        a, b, c, d = query[i].split(' and ')
        d, e = d.split()
        e = int(e)
        query_key_lst = [a, b, c, d]
        while '-' in query_key_lst:  # - 제거
            query_key_lst.remove('-')
        query_key = ''.join(query_key_lst)
        
        # query의 key값(query_key)이 info{}의 키값으로 존재하면 그 info딕셔너리의 value값들을 가져온 후
        # 가져온 value값들(점수)에서 기준 점수값을 넘는 것들의 개수 구하기 -> 이분탐색(binset_left)
        if query_key in info_dict:
            scores = info_dict[query_key]
            if scores:
                enter = bisect_left(scores, e)
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
            
    return answer
~~~
