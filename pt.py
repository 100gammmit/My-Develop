import sys

def binary_search(li, target):
    start = 0
    end = len(li) -1

    while start <= end:
        middle = (start+end)//2
        if li[middle]==target:
            return middle
        elif li[middle]>target:
            end = middle - 1
        else:
            start = middle + 1
    return -1

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
    while 1:
        if maxpo(target) in mmr:
            return mmr.index(target)
        else:
            if maxpo(target) > mmr[start]:
                    start+=1
                    continue
            mmr[start] = mmr[start]//2
            mmr.insert(start, mmr[start])

lst = list(map(int, sys.stdin.readline().split()))
memory = [minpo(lst.pop(0))]
idx=0
for i in lst:
    print(makebuddy(memory, i))
    print(memory)
    idx+=1