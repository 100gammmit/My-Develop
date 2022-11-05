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

def allocate(mmr, target):
    start = 0
    alloc_st = 0
    while 1:
        for i in range(len(mmr)):
            if target == mmr[i][1] and mmr[i][0] == 1:
                for j in range(i):
                    alloc_st += mmr[j][1]
                mmr[i][0] = 0
                return [alloc_st, alloc_st+mmr[i][1]-1]
            
        try:
            if mmr[start][0] == 0 or target > mmr[start][1]:
                start+=1
                continue
            mmr[start][1] = mmr[start][1]//2
            mmr.insert(start, [1, mmr[start][1]])
        except:
            return -1
        
def dellocate(mmr, alloc_mmr, start):
    for i in range(len(alloc_mmr)):
        if start == alloc_mmr[i][0]:                
            size = alloc_mmr[i][1]-alloc_mmr[i][0]+1
            start_lst=[]
            for t in alloc_mmr: 
                if t[1]-t[0]+1 == size: start_lst.append(t[0])
            tmp = sorted(start_lst).index(start)

            for j in range(len(mmr)):
                if size == mmr[j][1] and mmr[j][0] == 0:
                    if tmp == 0:
                        mmr[j][0] = 1
                        return alloc_mmr.pop(i)
                    else:
                        tmp -= 1
    return -1

def coalesce(mmr, idx):
    mmr[idx][1] *= 2
    mmr.pop(idx+1)

ipt_lst = list(map(int, sys.stdin.readline().split()))
lst=[]
memory = [[1, minpo(ipt_lst.pop(0))]]
alloc_mmr = []
for i in range(len(ipt_lst)):
    if i%2 == 0:
        lst.append([ipt_lst[i]])
    else:
        lst[i//2].append(ipt_lst[i])

for i in lst:
    if i[0] == 1:
        alloc = allocate(memory, maxpo(i[1]))
        if alloc == -1:
            print("Sorry, failed to allocate memory")
        else:
            alloc_mmr.append(alloc)
            print(f"Memory from {alloc[0]} to {alloc[1]} allocated")
    
    else:
        dealloc = dellocate(memory, alloc_mmr, i[1])
        if dealloc == -1:
            print("Sorry, invalid free request")
        else:
            print(f"Memory block from {dealloc[0]} to {dealloc[1]} freed")
            
            adrs = 0
            for j in range(0, len(memory)-1):
                if memory[j][1] == memory[j+1][1] and memory[j][0] == 1 and memory[j+1][0] == 1:
                    print(f"Coalescing of blocks starting at {adrs} and { adrs + memory[j][1] } was done")
                    coalesce(memory, j)
                    break
                adrs+=memory[j][1]
    print(alloc_mmr, memory)