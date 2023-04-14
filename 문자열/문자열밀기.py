def solution(A, B):
    answer = 0
    if A==B:
        return 0
    for i in range(len(A)-1):
        A= A[-1]+A[:-1]
        answer+=1
        
        if A==B:
            return answer

            
    answer=-1
    return answer
