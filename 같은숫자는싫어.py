def solution(arr):
    answer = []

    tmp=-1
    for i in arr:
        if i!=tmp:
            tmp = i
            answer.append(i)
            

    return answer
