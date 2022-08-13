# 2020 카카오 인턴십 - 수식 최대화

def solution(expression):
    answer = 0
    
    print(expression)

    op = []
    count = []
    num = ''
    for e in expression:
        if e == '+' or e == '-' or e == '*' :
            op.append(e)
            count.append(int(num))
            num = ''
        else:
            num += e
    count.append(int(num))
    
    print(op)
    print(count)
        
    
    return answer