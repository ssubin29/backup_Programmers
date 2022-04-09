# 깊이/너비 우선 탐색(DFS/BFS) - 타겟 넘버
from collections import deque

answer = 0
class Tree:
    def __init__(self, val = None):
        if val != None:
            self.val = val
        else:
            self.val = None

        self.left = None
        self.right = None

    def insert(self, val_list, target): # left right를 모두 채우는 insert
        if (val_list):
            val = val_list[0]
            self.left = Tree(self.val - val)            
            self.right = Tree(self.val + val)
            #print(self.left.val,self.right.val)
            self.left.insert(val_list[1:])
            self.right.insert(val_list[1:])  
        else:
            if target == self.val:
                answer +=1


def solution(numbers, target):
    
    tree = Tree(0) # 시작은 0
    tree.insert(numbers, target)

    return answer

#print('answer은', solution(	[1, 1, 1], 3))