from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while len(people)>1:
        
        if people[0]+people[-1]>limit:
            answer+=1
            people.pop()
        else:
            if people:
                answer+=1
                people.popleft()
                people.pop()
    if people:
        answer+=1
      
    return answer
