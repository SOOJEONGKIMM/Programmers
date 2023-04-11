def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    rocks.sort()
    while left <= right:
        mid = (left+right)//2
        del_rock_cnt=0
        start_rock=0
        for r in rocks:
            if r - start_rock < mid:
                del_rock_cnt += 1

            else:
                start_rock = r
                
            if del_rock_cnt > n:
                break
        if del_rock_cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
            
    
    return answer
