import sys
sys.setrecursionlimit(10**6)
def preorder(arrY, answer):
    cur = arrY[0]
    arrYleft, arrYright = [], []
    for i in range(1, len(arrY)):
        if cur[0] > arrY[i][0]:#x축
            arrYleft.append(arrY[i])
        else:
            arrYright.append(arrY[i])
    answer.append(cur[2])    #자기 왼 오
    if arrYleft:
        preorder(arrYleft, answer)
    if arrYright:
        preorder(arrYright, answer)  
    return 

def postorder(arrY,answer):
    cur = arrY[0]
    arrYleft, arrYright = [], []
    for i in range(1, len(arrY)):
        if cur[0] > arrY[i][0]:#x축
            arrYleft.append(arrY[i])
        else:
            arrYright.append(arrY[i])
    if arrYleft:
        postorder(arrYleft, answer)
    if arrYright:
        postorder(arrYright, answer) 
    answer.append(cur[2])   #왼 오 자기
    return 
def solution(nodeinfo):
    answer = []
    arrY = []
    pre_list, post_list = [], []
    for i in range(len(nodeinfo)):#노드번호 정보추가
        nodeinfo[i].append(i+1)
    arrY = sorted(nodeinfo, key = lambda x: (-x[1],x[0])) 
    preorder(arrY,  pre_list)
    postorder(arrY, post_list)
    answer.append(pre_list)
    answer.append(post_list)
    return answer
