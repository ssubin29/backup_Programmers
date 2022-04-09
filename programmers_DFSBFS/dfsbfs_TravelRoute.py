# 깊이/너비 우선 탐색(DFS/BFS) - 여행경로

from collections import deque
import sys
sys.setrecursionlimit(10**7)

# BFS 함수 정의
def bfs(dict_of_ticket, start, i, length, ans):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    ans.append(start)
    if start in dict_of_ticket.keys():
        if length == len(ans):
            print(ans)
        else:
            # 큐가 빌 때까지 반복
            while queue:
                # 큐에서 하나의 원소를 뽑아 출력
                start = queue.popleft()        
                for i in range(len(dict_of_ticket[start])):
                    bfs(dict_of_ticket, dict_of_ticket[start][i], i, length, ans)
            
        

def solution(tickets):
    answer = []
    dict_t = {} # tickets를 dict 형태로 변환
    
    for i in range(len(tickets)):
        if tickets[i][0] in dict_t.keys():
            dict_t[tickets[i][0]].append(tickets[i][1])
        else:
            dict_t[tickets[i][0]] = [tickets[i][1]]
    print(dict_t)
    
    length = len(dict_t.keys())    
    #visited = [False] * length
    answer = bfs(dict_t, "ICN", 0, length, answer)
        
    
    return answer