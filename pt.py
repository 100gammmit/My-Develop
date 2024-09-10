import sys

def minpo(target):
    i = 1
    while target >= i:
        i*=2
    return i//2
def maxpo(target):
    i = 1
    while target > i:
        i*=2
    return i

def makebuddy(mmr, target):
    start = 0
    alloc_st = 0
    while 1:
        for i in mmr:
            if target == i[0] and i[1] == 1:
                for j in range(0, mmr.index(i)):
                    alloc_st += mmr[j][0]
                i[1] = 0
            
                return [alloc_st, alloc_st+i[0]-1]
        try:
            if mmr[start][1] == 0 or target > mmr[start][0]:
                start+=1
                continue
            mmr[start][0] = mmr[start][0]//2
            mmr.insert(start, [mmr[start][0], 1])
        except:
            return -1

        
        

lst = list(map(int, sys.stdin.readline().split()))
memory = [[minpo(lst.pop(0)), 1]]

for i in lst:
    alloc_mmr = makebuddy(memory, maxpo(i))
    if alloc_mmr == -1:
        print 'Sorry, failed to allocate memory'
    else:
        print 'Memory from %d to %d allocated' %(alloc_mmr[0], alloc_mmr[1])
    #print(memory)