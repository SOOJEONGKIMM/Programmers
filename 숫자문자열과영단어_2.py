def solution(s):
    dic={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    answer=0
    for key, value in dic.items():
        if key in s:
            s = s.replace(key, str(value))
    answer=int(s)
    return answer
