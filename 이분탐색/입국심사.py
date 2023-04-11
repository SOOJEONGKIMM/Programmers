#이분탐색
def solution(n, times):
    answer = 0
    left, right = 0, max(times)*n
    while left <= right:
        mid = (left + right)//2
        people=0
        for t in times:
            people += mid // t #mid동안 심사한 사람 수 
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1 #이분탐색의 왼쪽으로 다시 탐색
        elif people < n:
            left = mid +1 #이분탐색의 오른쪽으로 다시 탐색 
            
    return answer
