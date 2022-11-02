import sys
sys.setrecursionlimit(10**6)
def preorder(arrY, arrX, answer):
    cur = arrY[0]
    arrYleft, arrYright = [], []
    idx = arrX.index(cur)
    for i in range(1, len(arrY)):
        if cur[0] > arrY[i][0]:#x축
            arrYleft.append(arrY[i])
        else:
            arrYright.append(arrY[i])
    answer.append(cur[2])    #자기 왼 오
    if arrYleft:
        preorder(arrYleft, arrX[:idx],answer)
    if arrYright:
        preorder(arrYright, arrX[idx+1:],answer)  
    return 

def postorder(arrY, arrX, answer):
    cur = arrY[0]
    arrYleft, arrYright = [], []
    idx = arrX.index(cur)
    for i in range(1, len(arrY)):
        if cur[0] > arrY[i][0]:#x축
            arrYleft.append(arrY[i])
        else:
            arrYright.append(arrY[i])
    if arrYleft:
        postorder(arrYleft, arrX[:idx],answer)
    if arrYright:
        postorder(arrYright, arrX[idx+1:],answer) 
    answer.append(cur[2])   #왼 오 자기
    return 
def solution(nodeinfo):
    answer = []
    arrY, arrX = [], []
    pre_list, post_list = [], []
    for i in range(len(nodeinfo)):#노드번호 정보추가
        nodeinfo[i].append(i+1)
    arrY = sorted(nodeinfo, key = lambda x: (-x[1],x[0]))
    arrX = sorted(nodeinfo)
    
    preorder(arrY, arrX, pre_list)
    postorder(arrY, arrX, post_list)
    answer.append(pre_list)
    answer.append(post_list)
    return answer
