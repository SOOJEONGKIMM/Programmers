#총 39분. 시간을 더 줄여야겠다. datetime 패키지 오랜만에 쓰려니 생각이 잘 안 났다.(자잘한 타입변환이 시간소모가 컸음)
#다른 풀이 보니 map함수 썼다.


import datetime
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):
    #day_per_month=[31,28,31,31,]
    answer = []
    terms_dict={}
    year, month, day = today.split('.')
    today = datetime.date(int(year), int(month), int(day))
    for i in terms:
        terms_dict[i.split()[0]]=i.split()[1]
    for idx, i in enumerate(privacies):
        date = i.split()[0]
        for k, v in terms_dict.items():
            if k==i.split()[1]:
                year, month, day = date.split('.')
                day_delta = datetime.date(int(year), int(month), int(day))
                #print(day_delta)
                
                final_day = day_delta + relativedelta(months=int(v))-relativedelta(days=1)
                #print(year, month, day, k,v, final_day, today)
                if final_day < today:
                    #print(final_day, today, idx+1)
                    answer.append(idx+1)
                
        
    return answer
