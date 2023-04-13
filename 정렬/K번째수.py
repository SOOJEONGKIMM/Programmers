def solution(array, commands):
    answer = []
    for c in commands:
        second = array[c[0]-1:c[1]]
        second.sort()
        third = second[c[2]-1]
        answer.append(third)
        
    return answer
