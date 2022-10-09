import time, threading
ra, rb = map(str, input('파일 이름을 입력하시오: ').split())

a_all = []
b_all = []
a_half1=[]
b_half1=[]
a_half2=[]
b_half2=[]

with open(ra) as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        a_all.append(list(map(int, line.split())))

with open(rb) as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        b_all.append(list(map(int, line.split())))

for i in range(0, 500):
    a_half1.append(a_all[i])
    b_half1.append(b_all[i])
for i in range(500, 1000):
    a_half2.append(a_all[i])
    b_half2.append(b_all[i])
        
def mulab1(result):    
    for i in range(1000):
        result.append(list())
        for j in range(1000):
            result[-1].append(a_all[i][j]*b_all[i][j])
    return

def mulab2(result):    
    for i in range(500):
        result.append(list())
        for j in range(1000):
            result[-1].append(a_half1[i][j]*b_half2[i][j])
    return

def mulab3(result):    
    for i in range(500):
        result.append(list())
        for j in range(1000):
            result[-1].append(a_half2[i][j]*b_half2[i][j])
    return

one_result=[]
mul1_result=[]
mul2_result=[]

one_start = time.perf_counter()
oneth = threading.Thread(target = mulab1, args=(one_result,))
oneth.start() 
oneth.join()
one_end = time.perf_counter()
print (f'단일스레드: {one_end - one_start} (초)')

mul_start = time.perf_counter()
multh1 = threading.Thread(target = mulab2, args=(mul1_result,))
multh2 = threading.Thread(target = mulab3, args=(mul2_result,))

multh1.start()
multh2.start() 
multh1.join()
multh2.join()

mul_end = time.perf_counter()
print (f'멀티스레드: {mul_end - mul_start} (초)')