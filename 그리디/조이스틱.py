def solution(name):
    answer = 0
    '''연속되는 A의 최대 길이가 핵심포인트.
    연속되는 A가 있는 곳에는 굳이 갈 필요가 없으므로, 그 부분을 제외하고 수정하는 경우를 계산한다.
    다만, 연속되는 A가 여러군데인 경우 가장 긴 부분을안가는게 더 효율적일 것이다. ex) JAAJAAAAJ 인 경우 4번째 J를 처리하기 위해서 2, 3번째의 연속된 AA를 건너는게 5,6,7,8번쨰의 연속된 AAAA를 건너는 것 보다 낫다.'''
    min_move = len(name)-1
    for i, char in enumerate(name):
        answer += min((ord(char)-ord('A')), ord('Z')-ord(char)+1)
        next = i+1
        while next<len(name) and name[next]=='A':
            next+=1
        min_move = min(min_move, 2*i+len(name)-next, 2*(len(name)-next)+i)
    answer+=min_move
        
    return answer
