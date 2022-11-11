S='LILLYBILLYBOO'
L=['BILL', 'MARIA', 'LILLY']
def solutionTask1(S, L):
    scnt = dict()
    maxret = 0

    for s in S:
        if s not in scnt.keys():
            scnt[s] = 1
        else:
            scnt[s] += 1
    print(scnt)

    for name in L:
        ncnt = dict()
        for c in name:
            if c not in ncnt.keys():
                ncnt[c] = 1
            else:
                ncnt[c] += 1
        print(name, ncnt)

        curret = 999
        for key in ncnt.keys():
            if key not in scnt.keys():
                curret = 0
                break

            

            print(key, scnt[key], ncnt[key], curret, scnt[key] // ncnt[key])
            curret = min(curret, scnt[key] // ncnt[key])

        maxret = max(maxret, curret)

    return maxret

print(solutionTask1(S,L))
