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
    
    
    tree = Tree(34)
    tree.insert(33)
    tree.insert(32)
    print(tree.val) #34
    print(tree.right) #None
    print(tree.left.val) #33
    print(tree.left.left.val) #32
    
    
    
    
    return answer

print([] == None)
print([3][1:])