# 그래프 - 순위

from collections import deque
import copy

# win_list로 lose_list 추론
def solution(n, edge):
    answer = 0
    edge.sort()    
    graph = [deque([]) for i in range(n+1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
    
    win_list =[]
    lose_list = [[] for i in range(n)]
    for i in range(1, n+1):  
        win = list(graph[i])
        queue = deque(graph[i])
        while queue:
            theN = queue.popleft()
            if graph[theN]  :
                for t in graph[theN]:
                    if t not in win:
                        queue.append(t)   
            if theN not in win:
                win.append(theN)
        win_list.append(win) 
        for w in win:
            lose_list[w-1].append(i)
        graph[i] = deque(win)
    
    # 기본적인 논리 구조는 이렇게
    # A 선수의 정확한 순위를 알기 위해선
    # 1. A 선수의 상대들 
    # 2. A 선수를 이긴 상대 중 그 상대에게 이긴 사람들
    # (상대하지 않아도 A의 순위가 낮다는 것을 알 수 있다.)
    # 3. A 선수에게 진 상대 중 그 상대에게 진 사람들
    # 1~3을 count했을 때 n-1명이면 된다!
    
    for i in range(n):     
        if  len(set(lose_list[i] + win_list[i])) == n-1:
            answer += 1
   
    return answer

#print(solution(5, [[1, 2], [4, 5], [3, 4], [2, 3]]))