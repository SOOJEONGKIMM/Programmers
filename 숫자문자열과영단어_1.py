def solution(s):
    hangul = ['zero','one', 'two','three','four', 'five', 'six', 'seven', 'eight', 'nine']
    arab = [i for i in range(len(hangul))]

    for h, a in zip(hangul, arab):
        s = s.replace(h, str(a))
    answer=int(s)
    return answer
