from itertools import product
def solution(word):
    answer = 0
    alph = ['A','E','I','O','U']
    ex_word=[]
    for i in range(1,6):
        for j in product(alph,repeat=i):
            ex_word.append(''.join(j))
            
            #ex_word+=''.join(product(alph[j],repeat=i))
    ex_word.sort()     
            
            
    #print(ex_word)
    answer = ex_word.index(word)+1
    #print(answer) 
    return answer
