import random
import decimal
slot=1000 # 상자 아이템 수
get=1 # 원하는 아이템이 나오는 범위
seg=list(range(1,get+1))
rotation=100 #시뮬레이션 횟수
s=0
r=0
for i in range(rotation):
    cnt=0 # 원하는 아이템이 걸리는 횟수
    arr=list(range(1,slot+1))
    random.shuffle(arr)
    while 1:
        if len(arr)==0:break
        if 1<=arr[0]<=get:break
        random.shuffle(arr)
        arr.pop(0)
        cnt+=1
    s+=cnt
    r+=cnt*(get/slot)
    print(f'{i+1}번째 case : {cnt}')
print(f'확률 {get/slot*100}% 에 대한 종합 평균값 : {s/rotation}')
print(f'확률 {get/slot*100}% 에 대한 종합 기댓값 : {r}')
