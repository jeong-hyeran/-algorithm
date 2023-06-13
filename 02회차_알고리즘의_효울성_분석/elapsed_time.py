#속도를 측정하고자 하는 알고리즘
def find_max(A) :
    max = A[0]
    for item in A :
        if item > max :
            max = item
    return max

#실행 시간 측정 프로그램
import time

array = [ 1,4,8,3,4,2,4,5,9,5,3]

start = time.time()         #현재시간을 저장
max = find_max(array)       #실행 시간을 측정하려는 코드
end = time.time()           #현대 시간을 저장

print("최대값 =", max)
print("실행시간 =", end-start) #실행 시간(종료-시작)을 출력

#================================
import random
array = [random.randint(0,10000)for i in range(10000)]

start = time.time()         #현재시간을 저장
for n in range(10000) :
    max = find_max(array)       
end = time.time()           #현대 시간을 저장

print("최대값 =", max)
print("실행시간 =", end-start) #실행 시간(종료-시작)을 출력
