def solution(nums):
    answer = 0
    take = int(len(nums)/2)
    s = set(nums)
    if len(s)<=take:
        answer = len(s)
    else:
        answer = take
        
return answer

