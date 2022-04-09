# 깊이/너비 우선 탐색(DFS/BFS) - 타겟 넘버

# 사용할 이진트리 정의
class Tree:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val_list): # left right를 모두 채우는 insert
        if (val_list):
            val = val_list[0]
            self.left = Tree(self.val - val)            
            self.right = Tree(self.val + val)
            self.left.insert(val_list[1:])
            self.right.insert(val_list[1:])      

# BFS 함수 정의
def dfs(node, target, depth, goal):
    count = 0
    if (depth == goal):
        if(node.val == target):
        # 노드의 왼쪽에 있는 노드들 중 끝에 있으면서(depth == goal)
        #target과 같은 값인 수 반환
            return 1 
        else:
            return 0
    else :
        if node.left != None:
            count += dfs(node.left, target, depth+1, goal)
            count += dfs(node.right, target, depth+1, goal)        
    return count      

def solution(numbers, target):
    answer = 0
    
    tree = Tree(0) # 시작은 0
    tree.insert(numbers)

    answer += dfs(tree, target, 0, len(numbers))

    return answer
