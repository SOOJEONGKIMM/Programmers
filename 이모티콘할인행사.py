from itertools import product
def solution(users, emoticons):
    answer = [-1,-1]
    for discount in (product([10,20,30,40], repeat=len(emoticons))):
        new_users=0
        total_cost=0
        for user in users:
            buy_cost=0
            for i in range(len(discount)):
                if discount[i]>=user[0]:
                    buy_cost+=(emoticons[i]*(1-discount[i]/100))
            if buy_cost >= user[1]:
                new_users+=1
                buy_cost=0
            total_cost += buy_cost
            
        if answer[0] < new_users:
            answer[0]=new_users
            answer[1]=total_cost
        elif answer[0]==new_users:
            answer[1]=max(total_cost, answer[1])
                    
            
            
    return answer
