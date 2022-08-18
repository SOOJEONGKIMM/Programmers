def solution(board, moves):
    answer = 0
    stack=[]
    for m in moves:
        m-=1
        for i in range(len(board)):
            if board[i][m]!=0:
                stack.append(board[i][m])
                board[i][m]=0
                
                if stack[-1:]==stack[-2:-1]:
                    stack=stack[:-2]
                    answer+=2
                break
        #print(board, stack)
    return answer
