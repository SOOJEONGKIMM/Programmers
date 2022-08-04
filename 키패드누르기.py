
def solution(numbers, hand):
    answer = ''
    lefthand=[1,4,7]
    righthand=[3,6,9]
    middle=[2,5,8,0]
    left_index=10
    right_index=12 #키패드 * 을 10, 0을 11, #을 12
    for i in numbers:
        if i in lefthand:
            answer+='L'
            left_index=i
        elif i in righthand:
            answer+='R'
            right_index=i
        else:
            i=11 if i==0 else i
            left_distance=abs(int(left_index)-i)
            right_distance=abs(int(right_index)-i)
            
            if sum(divmod(left_distance,3)) > sum(divmod(right_distance,3)):
                answer+='R'
                right_index=i
            elif sum(divmod(left_distance,3)) < sum(divmod(right_distance,3)):
                answer+='L'
                left_index=i
            else:
                if hand=="right":
                    answer+='R'
                    right_index=i
                else:
                    answer+='L'
                    left_index=i
            
    
    
    return answer
