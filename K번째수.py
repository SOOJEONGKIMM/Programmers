def solution(array, commands):
    answer = []
    for a in commands:
        tmp = sorted(array[a[0]-1:a[1]])
        answer.append(tmp[a[2]-1])
    return answer
