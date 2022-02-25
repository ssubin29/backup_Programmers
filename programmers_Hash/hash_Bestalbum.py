def solution(genres, plays):
    answer = []
    play_count = {} # genre가 key, play의 총합이 value
    genre_count = {} # genre가 key (고유번호,play) 튜플이 value
    
    for i in range(len(plays)):
        
        if genres[i] not in play_count.keys():
            play_count[genres[i]]=plays[i]
            genre_count[genres[i]]=[(i,[plays[i]])]
        else:
            play_count[genres[i]]=play_count[genres[i]]+plays[i]
            genre_count[genres[i]].append((i,[plays[i]]))
            
            
    play_count = sorted(play_count.items(), 
                        key = lambda item: item[1], reverse = True)
    
    
    
    for key in play_count:
        # key[1]이 genre
        
        
    print(play_count)
    print(genre_count)
    
    return answer