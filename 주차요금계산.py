
from collections import Counter
from datetime import datetime
import math
def solution(fees, records):
    answer = []
    basic_time, basic_fee, unit_time, unit_fee = fees
    re = {}
    parking_time = {}
    for i in range(len(records)):
        time, num, inout =records[i].split()
        if inout=="IN":
            re[num]=time
        else:
            intime = datetime.strptime(re[num], "%H:%M")
            outtime = datetime.strptime(time, "%H:%M")
            r = (outtime - intime).seconds/60
            try:
                parking_time[num]+=r
            except:
                parking_time[num]=r
            del re[num]
    for k, v in re.items():
        intime = datetime.strptime(v, "%H:%M")
        outtime = datetime.strptime("23:59", "%H:%M")
        r = (outtime - intime).seconds/60
        try:
            parking_time[k]+=r
        except:
            parking_time[k]=r
    parking_time = sorted(list(parking_time.items()), key=lambda x: x[0])
    for k, v in parking_time:
        t = fees[1] + math.ceil(max(0,(v-fees[0]))/fees[2])*fees[3]
        answer.append(t)
    return answer
