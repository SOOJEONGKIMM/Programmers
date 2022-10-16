import itertools 
def solution(n):
    answer = ''
    nara = ['1','2','4']

    while n>0:
        n-=1
        answer = nara[n%3] + answer
        print(answer)
        n//=3

    return answer

