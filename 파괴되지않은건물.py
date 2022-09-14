
def solution(board, skill):
    answer = 0
    tmp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)] #누적합으로 풀어야 효율성테스트 통과함. 
    
    for what, l1, r1, l2, r2, much  in skill:
        for y in range(l1, l2+1, 1):
            for x in range(r1, r2+1, 1):
                if what==2: 
                    board[y][x]+=much
                else:
                    board[y][x]-=much
    for i in board:
        i.sort(reverse=True)
        for j in i:
            if j <= 0:
                break
            answer+=1
    return answer
