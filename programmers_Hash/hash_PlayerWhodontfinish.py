def solution(participant, completion):
    # 1. 두 list를 sort 
    participant.sort(); completion.sort();
    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다 
    # 이 경우엔 AABC ABC 일 경우를 잡아낼 수 있음
    for i in range(len(completion)): 
        if(participant[i] != completion[i]): 
            return (participant[i])
    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    # 2번으로도 잡히지 않은 경우 : ABCD ABC (ABC까지 모두 같으므로 for문을 통과한다)
    return participant[len(participant)-1]
