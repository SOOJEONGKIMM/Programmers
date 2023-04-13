import heapq
def solution(operations):
    answer = []
    heap = []
    for o in operations:
        if o=="D 1":
            if heap:
                heap.sort(reverse=True)
                heapq.heappop(heap)
        elif o=="D -1":
            if heap:
                heap.sort(reverse=False)
                print(heap)
                heapq.heappop(heap)
        else:
            delimeter, insert_num = o.split(' ')
            heapq.heappush(heap, int(insert_num))

        
    if not heap:
        answer = [0,0]
    else:
        answer = [max(heap),min(heap)]
    return answer
