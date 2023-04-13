def solution(numbers):
    answer = ''
    nums = list(map(str, numbers))
    nums.sort(key=lambda x: x*3, reverse=True) #1000이하의 nums
    answer = str(int(''.join(nums))) #000처리 
    return answer
