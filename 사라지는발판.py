move = ((1,0),(0,1),(-1,0),(0,-1))
def a_turn(ar,ac,br,bc,cnt,board):
    if board[ar][ac]==0:
        return(1,cnt)
    winner,loser=[],[]
    flag=False
    for dr, dc in move:
        nr, nc = ar+dr, ac+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]):
            if board[nr][nc]==1:
                flag=True
                tmp=[row[:] for row in board]
                tmp[ar][ac]=0
                iswin, turn = b_turn(nr,nc,br,bc,cnt+1,tmp)
                if iswin:
                    winner.append(turn)
                else:
                    loser.append(turn)
    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)

def b_turn(ar,ac,br,bc,cnt,board):
    if board[br][bc]==0:
        return (1,cnt)
    flag=False
    winner, loser =[],[]
    for dr, dc in move:
        nr, nc = br+dr, bc+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]):
            if board[nr][nc]==1:
                flag=True
                tmp=[row[:] for row in board]
                tmp[br][bc]=0
                iswin, turn = a_turn(ar,ac,nr,nc,cnt+1,tmp)
                if iswin:
                    winner.append(turn)
                else:
                    loser.append(turn)
                    
    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)
                
    
def solution(board, aloc, bloc):
    answer = -1
    ar, ac, br, bc = aloc[0], aloc[1], bloc[0], bloc[1]
    answer = a_turn(ar,ac,br,bc,0,board)[1]
    return answer
