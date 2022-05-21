# DP가 적용되기 위한 2가지 조건
# 1) Overlapping Subproblem (겹치는 부분 문제)
# 동일한 작은 문제들이 반복하여 나타는 경우에 사용이 가능하다
# 2) Optimal Substructure (최적 부분 구조)
# 부분 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있는 경우

# DP를 사용하기 전 해야할 일
# 1) DP로 풀 수 있는 문제인지 확인한다.
# 2) 문제의 변수 파악
# 3) 점화식 만들기 (피보나치의 경우 f(n) = f(n-1) + f(n-2)
# 4) 메모 memorization 변수 값에 따른 결과를 저장할 배열을 미리 만든다
# 5) 기저 상태 (가장 작은 문제의 상태) 파악 후 미리 배열에 저장
# 6) 구현 (반복문을 사용하는 Bottom-Up, 재귀를 사용하는 Top-Down)

# DP 
# memoization (하향식)

fac = [0]*100 # 소문제 결과를 저장할 리스트
fac[0] = 1 
fac[1] = 1

def factorial(n):
    
    # 만약 계산한 적이 없다면 재귀로 계산 
    if fac[n] == 0:
        fac[n] = factorial(n-1)*n    
    # 있다면 그대로 반환 
    return fac[n]
