# [Programmers 42892: 길 찾기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/42892)

`#BinaryTree` `#Preorder` `#Postorder`
---

## 접근
- 완전 자료구조 문제
- 이진 트리 구현하는게 전부 그리고 어려움
- 노드 좌표 정렬부터
    - 이진트리 위에서부터, 왼쪽에서부터 채워넣음!

## 풀이
### 노드 좌표 정렬
이진트리는 위에서부터, 왼쪽에서부터 채워넣는다  
- x를 먼저 오름차순 정렬
- y 내림차순 정렬
하여 node_info를 재정렬해준다.

### 노드 생성
노드는 클래스로 만들어주는게 편함

### 이진트리 생성
- 매 케이스 root 노드부터 시작
- current node가 pre node의 자식 노드에 들어갈 자리가 있는지 확인하며 추가해줌

### 전위순회, 후위순회
- 전위순회: 자기자신 방문 후 left, right 방문
- 후위순회: left, right 방문 후 자기자신 방문

---

## 전체 코드

```python
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def preorder(self, n):
        if n != None:
            order1.append(n.item[0])
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            order2.append(n.item[0])
    
def solution(nodeinfo):
    # 노드이름, 노드값 dic에 저장
    dic = []
    for i in range(1, len(nodeinfo)+1):
        dic.append((i, nodeinfo[i-1]))
    
    # 노드 우선순위 부여
    # x좌표 오름차순 정렬
    dic = sorted(dic, key = lambda x:x[1][0])
    # y좌표 내림차순 정렬
    dic = sorted(dic, key = lambda x:x[1][1], reverse=True)
    
    # 노드 생성
    nodes = []
    for i in range(len(nodeinfo)):
        nodes.append(Node(dic[i]))

    # 이진트리 생성
    tree = BinaryTree(nodes[0])
    for node in nodes[1:]:
        # 새 노드의 위치 탐색할때 pre_node는 다시 root부터 시작
        pre_node = tree.root
        while True:
            # 현재 노드가 이전 노드의 왼쪽에 있다면: left, 오른쪽에 있다면: right
            if node.item[1][0] < pre_node.item[1][0]:
                # 왼쪽에 아직 노드 없으면 현재 노드 추가하고 break -> 그 다음 노드가 오른쪽에 들어갈 수 있는지 체크
                if pre_node.left == None:
                    pre_node.left = node
                    break
                # 왼쪽에 노드 있으면 그 노드를 pre_node로 설정하고 다시 한바퀴
                else:
                    pre_node = pre_node.left
            else:
                # 오른쪽에 아직 노드 없으면 현재 노드 추가
                if pre_node.right == None:
                    pre_node.right = node
                    break
                # 오른쪽에 노드 있으면 그 노드를 pre_node로 설정하고 다시 한바퀴
                else:
                    pre_node = pre_node.right
    
    answer = []
    
    # 전위 순회
    global order1
    order1 = []
    tree.preorder(tree.root)
    answer.append(order1)
    
    # 후위 순회
    global order2 
    order2 = []
    tree.postorder(tree.root)
    answer.append(order2)
    
    return answer
```

- class를 잘 활용하면 더 좋은 코드가 될 것 같다
- 자료구조 공부도 열심히 하자