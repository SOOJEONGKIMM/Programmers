def solution(absolutes, signs):
    answer = 123456789
    sum=0
    for a, s in zip(absolutes, signs):
        if s:
            sum+=a
        else:
            sum=sum-a
    answer=sum
    return answer
