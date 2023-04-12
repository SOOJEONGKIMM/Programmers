def solution(brown, yellow):
    answer = []
    total = yellow + brown # == a*b
    for b in range(1, total+1):
        if total % b == 0:
            a = total // b
            if a * b == total:
                if 2*a + 2*b -4 ==brown:
                    if a*b - 2*a - 2*b +4 ==yellow:
                        answer = [a,b]
                        break
    return answer
