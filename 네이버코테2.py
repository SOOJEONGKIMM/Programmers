A=[2, 3, 1, 4, 2, 2]
R=3

minidx, minuniq = 0, 2e9
curcnt = dict()

# 초기값
for a in A[:R]:
    if a not in curcnt.keys():
        curcnt[a]=1
    else:
        curcnt[a]+=1
print(curcnt)

for i in range(len(A)-R):
    curuniq = len(list(curcnt.keys()))
    if curuniq < minuniq:
        minuniq = curuniq
        minidx = i

    print(i, curuniq, minuniq)

    curkey, nextkey = A[i], A[R+i]
    if curcnt[curkey] == 1:
        del curcnt[curkey]
    else:
        curcnt[curkey]-=1


    if nextkey not in curcnt.keys():
        curcnt[nextkey]=1

    else:
        curcnt[nextkey] +=1
    print(curkey, nextkey, curcnt)

    print(A[minidx: minidx+R])
