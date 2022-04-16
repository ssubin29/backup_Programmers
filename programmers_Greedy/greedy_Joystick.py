# 탐욕법 - 조이스틱

import itertools
import copy
    
# 최단 경로를 찾아주는 함수
# 입력값 : 시작 인덱스, 목표 인덱스, 총 길이
def get_better_way(start, des, limit_len): 
    better = 0
    a = abs(des-start) # A~Z 사이를 왔다갔다 ex)'A'>'C'는 이게 좋음
    b = start + (limit_len - des) + 1 # Z를 넘아 A부터 ex) 'Z'>'C'는 이게 좋음
    return a if a < b else b # 작은 거리 반환

def solution(name):
    answer = 0
    # A는 65 Z는 90
    
    # 알파벳과 알파벳이 위치해있는 인덱스 매핑
    indexing_list = {}
    for i in range(len(name)):
        if not name[i] in indexing_list.keys():
            indexing_list[name[i]] = [i]
        else:
            indexing_list[name[i]].append(i)
    print(indexing_list)

    # 중요한 것은 여기서 세는 것은 오직 조이스틱을 위아래로 조작한 횟수 뿐이다.
    alpha_len = ord('Z')-ord('A')
    updown_count = 0
    for alpha in name:
        updown_count = updown_count + get_better_way(0, ord(alpha)-ord('A'), alpha_len)    
    answer += updown_count  
    
    # 지금부터는 상하로 조작하는 횟수만 카운트한다.
    # 여기서 주의! 문자열에 A가 없다면 문자열의길이-1이 상하조작 횟수지만
    # 붙어있는 A가 있다면(두 세트 이상부터는 상관x) 그 부분은 조작할 필요가 없으니까 그 부분을 뺴고 왼쪽으로 돌게 된다
    Acount = 0
    opened = False # CAAT 처럼 A가 한 세트 연달아 있을 때
    closed_by_A = False # 말그대로 A 세트가 앞뒤에만 있을 때 AADFA cf)ABSTRACTA
    if 'A' in indexing_list.keys():
        A_list = indexing_list['A']       

        # opened부터 판별
        if len(A_list) == 1:
            Acount += 1
            opened = True
        else:
            a = [i for i in range(len(name))]
            s = A_list[0]
            e = A_list[-1]
            print(A_list)
            if A_list == a[A_list[0]:A_list[-1]+1]:
                Acount = len(A_list)
                opened = True
        if (opened):
            print('opened입니다')
            return answer + (len(name) - 1 ) - Acount
        print('opened는 아닙니다')

        # closed_by_A 판별
        A_list = indexing_list['A']
        if (0 in A_list) and (len(name)-1 in A_list):
            c = 0
            for a_index in A_list[1:]:
                if c + 1 == a_index:
                    A_list.remove(c+1)
                    Acount += 1
                    c = a_index
                else:
                    break
            for a_index in A_list[::-1]:
                if c - 1 == a_index:
                    A_list.remove(c-1)
                    Acount += 1
                    c = a_index
                else:
                    break
            if not (A_list):
                closed_by_A = True
        if (closed_by_A):
            #print('closed_by_A입니다')
            return answer + (len(name) - 1 ) - Acount        
        #print('closed_by_A 또한 아닙니다')
        
    return answer + (len(name) - 1 )

print(solution("BBAAAACC"))