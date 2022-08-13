# 2020 카카오 인턴십 - 수식 최대화
from itertools import combinations, permutations


def solution(expression):
    answer = 0
    
    ops = []
    nums = []
    num = ''
    count = 0
    op_list = {} # dict 형태로 '연산자 or 숫자' : 인덱스 번호
    for e in expression:
             
        if e == '+' or e == '-' or e == '*' :
            ops.append(e)
            nums.append(int(num))
            if e in op_list.keys():
                op_list[e].append(count+1)
            else:
                op_list[e] = [count+1]   
            count +=1    
            if num in op_list.keys():
                op_list[num].append(count+1)
            else:
                op_list[num] = [count+1] 
            num = ''
            count +=1 
        else:
            num += e  
        
        
    nums.append(int(num))
    if num in op_list.keys():
        op_list[num].append(count+1)
    else:
        op_list[num] = [count+1]  
    
    print(op_list)
    perm = list(permutations(list(set(ops))))
    # perm = op의 우선순위 가짓수
        
    #for per in perm: # 가짓수 하나하나 세보기
        
    
    return answer