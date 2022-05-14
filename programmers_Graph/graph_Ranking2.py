# 그래프 - 가장 먼 노드
from collections import deque
import copy

def solution(n, edge):
    answer = 0
    edge.sort()    
    graphs = [deque([]) for i in range(n+1)]
    
    for e in edge:
        graphs[e[0]].append(e[1])
    #print(graphs)
    
    def bfs(queue, win):
        while queue:
            next = queue.popleft()
            win.append(next)
            win = bfs(graph[next],win)
        return win
    
    win_list =[]
    for i in range(1, len(edge)+1):
        graph = copy.deepcopy(graphs)
        win = list(graph[i])
        queue = deque(graph[i])
        win = bfs(queue,win)    
        win_list.append(list(set(win)))
    
    print(win_list)
    
    # 기본적인 논리 구조는 이렇게
    # A 선수의 정확한 순위를 알기 위해선
    # 1. A 선수의 상대들 
    # 2. A 선수를 이긴 상대 중 그 상대에게 이긴 사람들
    # (상대하지 않아도 A의 순위가 낮다는 것을 알 수 있다.)
    # 3. A 선수에게 진 상대 중 그 상대에게 진 사람들
    # 1~3을 count했을 때 n-1명이면 된다!
    
    match = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for win in win_list[i]:
            match[i][win-1] = 1
            match[win-1][i] = -1
    
    
    for m in match:
        count = 0
        for n in m:
            if n == 0:
                count += 1
        if count == 1:
            answer += 1
   
    return answer