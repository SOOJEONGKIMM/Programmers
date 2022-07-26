def solution(priorities, location):
    answer = 0
    priorities = [(pr,idx) for idx, pr in enumerate(priorities)]

    while priorities:
        cur = priorities.pop(0)
        if priorities and cur[0] < max(priorities)[0]:
            priorities.append(cur)
        else:
            answer += 1
            if cur[1]==location:
                break
    return answer
