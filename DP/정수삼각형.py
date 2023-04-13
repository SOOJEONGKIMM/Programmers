def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1], triangle[i-1][j])
            #print(i,j,triangle[i][j],triangle)
    return max(triangle[-1])
