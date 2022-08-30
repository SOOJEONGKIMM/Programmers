def bfs(numbers, target, summ):
    if numbers==[]:
        if summ==target:
            return 1
        else:
            return 0
    return bfs(numbers[1:], target, summ+numbers[0])+bfs(numbers[1:], target, summ-numbers[0])
def solution(numbers, target):
    return bfs(numbers, target, 0)
