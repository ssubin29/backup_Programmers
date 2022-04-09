# 깊이/너비 우선 탐색(DFS/BFS) - 타겟 넘버

class Tree:
    def __init__(self, val = None):
        if val != None:
            self.val = val
        else:
            self.val = None

        self.left = None
        self.right = None
    def insert(self, val):
          if self.val:
              if val < self.val:
                    if self.left is None:
                        self.left = Tree(val)
                    else:
                        self.left.insert(val)
              elif val > self.val:
                    if self.right is None:
                        self.right = Tree(val)
                    else:
                        self.right.insert(val)
          else:
            self.val = val
            
def solution(numbers, target):
    answer = 0
    
    
    tree = Tree()
    tree.val = numbers[0]
    tree.left = numbers[0]+1
    tree.right = numbers[0]-1
    Tree.insert(33)
    print(tree.left)
    print(tree.right)
    print(tree.val)
    
    
    return answer