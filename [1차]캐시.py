def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize==0:
        return 5*len(cities)
    for c in cities:
        c = c.upper()
        if c not in cache:
            answer+=5
            if len(cache)<cacheSize:
                cache.append(c)
            else:
                cache.pop(0) #LRU
                cache.append(c)
        else:
            cache.remove(c) #LRU_스택에 있는 애도 위치재조정해줘야함!!
            cache.append(c)
            answer+=1
        #print(cache,answer)
    return answer

