
from collections import deque
def isbalanced(w):
    left, right =0,0
    for i in w:
        if i=='(':
            left+=1
        else:
            right+=1
    if left==right:
        return True
    else:
        return False
def solution(s):
    answer = True
    if not isbalanced(s):
        return False
    stack=deque()
    for i in s:
        if i=="(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.popleft()
    return True
