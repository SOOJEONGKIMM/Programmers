def solution(n, arr1, arr2):
    answer = []
    for a1,a2 in zip(arr1,arr2):
        b_num1 = format(a1,'b')
        b_num2 = format(a2,'b')

        b_num = int(b_num1)+int(b_num2)
        b_num = str(b_num)
        if len(b_num)<n:
            b_num = '0'*(n-len(b_num)) + str(b_num)
        b_num = b_num.replace('1','#')
        b_num = b_num.replace('2','#')
        b_num = b_num.replace('0',' ')
        answer.append(b_num)
    return answer


